#!/usr/bin/python3

import os
import gi
import json
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite, Gio, Pango
from datetime import timedelta, date
from appdirs import *

try:
    import constants as cn
except ImportError:
    import invoicy.constants as cn

class Invoice(Gtk.Box):
    status = False

    def __init__(self, parent):

        settings = Gio.Settings('com.github.maltekiefer.invoicy')
        with open(
                user_data_dir(cn.App.application_id, cn.App.application_name) +
                "/customers.json", "r") as read_file:
            cus_data = json.load(read_file)

        Gtk.Box.__init__(self, False, 0)
        self.parent = parent
        self.set_border_width(10)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        due_date = date.today() + timedelta(
            days=settings.get_uint('invoice-due-days'))

        btn_create_invoice = Gtk.Button.new_with_label("Create Invoice")
        btn_cancel = Gtk.Button.new_with_label("Cancel")
        btn_cancel.connect("clicked", self.btn_cancel_clicked)

        self.btn_create_pos = Gtk.Button()
        self.btn_create_pos.set_image(Gtk.Image(stock=Gtk.STOCK_ADD))
        self.btn_create_pos.connect("clicked", self.add_cb)

        self.btn_delete_pos = Gtk.Button()
        self.btn_delete_pos.add(Gtk.Image.new_from_gicon(Gio.ThemedIcon(name="user-trash"), Gtk.IconSize.LARGE_TOOLBAR))
        self.btn_delete_pos.connect("clicked", self.remove_cb)

        invoice_label = Gtk.Label()
        invoice_label.set_markup("<big><b>Invoice</b></big>")
        invoice_label.set_justify(Gtk.Justification.CENTER)

        cus_store_label = Gtk.Label("Customer")
        cus_store_combo = Gtk.ComboBoxText()

        for cus in cus_data:
            cus_store_combo.insert(
                int(cus['customer_id']), str(cus['customer_id']),
                cus['Company'] + " - " + cus['Contact'])

        invoice_number_label = Gtk.Label("Invoice #", xalign=0)
        invoice_number_entry = Gtk.Entry()
        invoice_date_label = Gtk.Label("Invoice Date", xalign=0)
        invoice_date_entry = Gtk.Entry()
        invoice_date_entry.set_text(date.today().strftime(
            settings.get_string('invoice-date-format')))
        invoice_due_label = Gtk.Label("Invoice Due", xalign=0)
        invoice_due_entry = Gtk.Entry()
        invoice_due_entry.set_text(
            due_date.strftime(settings.get_string('invoice-date-format')))
        invoice_note_label = Gtk.Label( xalign=0)
        invoice_note_label.set_markup("<big><b>Note: </b></big>")
        invoice_note = Gtk.TextView()
        invoice_note.set_cursor_visible(True)
        invoice_note.set_size_request(-1, 75)

        grid_invoice = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid_invoice.props.margin_left = 20
        grid_invoice.props.margin_right = 20
        grid_invoice.props.margin_top = 20
        grid_invoice.props.margin_bottom = 20

        grid_invoice.attach(invoice_label, 0, 1, 10, 1)

        grid_invoice.attach(cus_store_label, 0, 2, 1, 1)
        grid_invoice.attach(cus_store_combo, 1, 2, 1, 1)

        grid_invoice.attach(invoice_date_label, 3, 2, 1, 1)
        grid_invoice.attach(invoice_date_entry, 4, 2, 1, 1)

        grid_invoice.attach(invoice_number_label, 0, 3, 1, 1)
        grid_invoice.attach(invoice_number_entry, 1, 3, 1, 1)

        grid_invoice.attach(invoice_due_label, 3, 3, 1, 1)
        grid_invoice.attach(invoice_due_entry, 4, 3, 1, 1)

        btn_box = Gtk.Box(spacing=6)
        btn_box.props.margin_top = 20
        btn_box.pack_end(btn_create_invoice, False, True, 0)
        btn_box.pack_end(btn_cancel, False, True, 0)

        self.listmodel = Gtk.ListStore(str, str, str, str, str  )

        self.view = Gtk.TreeView(self.listmodel)
        for i, column_title in enumerate(
            ["Description", "Unity", "Quantity", "Price", "Total"]):
            column = Gtk.TreeViewColumn(column_title,
                                        Gtk.CellRendererText(),
                                        text=i)
            column.set_resizable(True)
            if i == 0:
                column.set_min_width(250)
                column.set_fixed_width(300)
            else:
                column.set_min_width(20)
                column.set_fixed_width(80)
            column.set_expand(False)
            self.view.append_column(column)

        self.selection = self.view.get_selection()

        self.invoice_net = Gtk.Label(xalign=0)
        self.invoice_net.set_markup("<b>Net</b>")
        self.invoice_net_sum = Gtk.Entry(xalign=1)
        self.invoice_net_sum.set_sensitive(False)

        self.invoice_tax = Gtk.Label(xalign=0)
        self.invoice_tax.set_markup("<b>Tax</b>")
        self.invoice_tax_sum = Gtk.Entry(xalign=1)
        self.invoice_tax_sum.set_sensitive(False)

        self.invoice_total = Gtk.Label(xalign=0)
        self.invoice_total.set_markup("<b>Total</b>")
        self.invoice_total_sum = Gtk.Entry(xalign=1)
        self.invoice_total_sum.set_sensitive(False)

        invoice_total = Gtk.Grid(column_spacing=2, row_spacing=2)
        invoice_total.props.margin_left = 20
        invoice_total.props.margin_right = 20
        invoice_total.props.margin_top = 20
        invoice_total.props.margin_bottom = 20

        invoice_total.attach(self.invoice_net, 0, 1, 1, 1)
        invoice_total.attach(self.invoice_net_sum, 1, 1, 1, 1)
        if settings.get_boolean('tax-on-invoice'):
            invoice_total.attach(self.invoice_tax, 0, 2, 1, 1)
            invoice_total.attach(self.invoice_tax_sum, 1, 2, 1, 1)
            invoice_total.attach(self.invoice_total, 0, 3, 1, 1)
            invoice_total.attach(self.invoice_total_sum, 1, 3, 1, 1)
        else:
            invoice_total.attach(self.invoice_total, 0, 2, 1, 1)
            invoice_total.attach(self.invoice_total_sum, 1, 2, 1, 1)

        btn_box_price = Gtk.Box(spacing=3)
        btn_box_price.props.margin_top = 20
        btn_box_price.pack_end(invoice_total, False, True, 0)

        btn_box_pos = Gtk.Box(spacing=3)
        btn_box_pos.props.margin_top = 20
        btn_box_pos.pack_end(self.btn_create_pos, False, True, 0)
        btn_box_pos.pack_end(self.btn_delete_pos, False, True, 0)

        self.add(grid_invoice)
        self.add(self.view)
        self.add(btn_box_price)
        self.add(btn_box_pos)
        if settings.get_boolean('invoice-note'):
            self.add(invoice_note_label)
            self.add(invoice_note)

        self.add(btn_box)


    def btn_cancel_clicked(self, button):
        self.parent.stack.set_visible_child_name("welcome")

    def add_cb(self, button):

        settings = Gio.Settings('com.github.maltekiefer.invoicy')
        dialog = Gtk.Dialog()
        dialog.set_transient_for(self.parent.parent)
        dialog.set_default_size(300, 300)
        dialog.set_modal(True)
        dialog.add_button(button_text="Cancel", response_id=Gtk.ResponseType.CANCEL)
        dialog.add_button(button_text="Save", response_id=Gtk.ResponseType.OK)

        pos_desc_label = Gtk.Label("Description")
        pos_desc_entry = Gtk.Entry()

        pos_quantity_label = Gtk.Label("Quantity")
        pos_quantity_entry = Gtk.Entry()

        pos_unity_label = Gtk.Label("Unity")
        pos_unity_entry = Gtk.Entry()

        pos_price_label = Gtk.Label("Price")
        pos_price_entry = Gtk.Entry()

        grid_pos = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid_pos.props.margin_left = 20
        grid_pos.props.margin_right = 20
        grid_pos.props.margin_top = 20
        grid_pos.props.margin_bottom = 20

        grid_pos.attach(pos_desc_label, 0, 1, 1, 1)
        grid_pos.attach(pos_desc_entry, 1, 1, 1, 1)
        grid_pos.attach(pos_unity_label, 0, 2, 1, 1)
        grid_pos.attach(pos_unity_entry, 1, 2, 1, 1)
        grid_pos.attach(pos_quantity_label, 0, 3, 1, 1)
        grid_pos.attach(pos_quantity_entry, 1, 3, 1, 1)
        grid_pos.attach(pos_price_label, 0, 4, 1, 1)
        grid_pos.attach(pos_price_entry, 1, 4, 1, 1)

        box = dialog.get_content_area()

        box.add(grid_pos)

        dialog.show_all()
        return_code = dialog.run()

        if return_code == Gtk.ResponseType.CANCEL:
            dialog.destroy()
        if return_code == Gtk.ResponseType.OK:

            desc = pos_desc_entry.get_text()
            unity = pos_unity_entry.get_text()
            quantity = pos_quantity_entry.get_text()
            price = pos_price_entry.get_text()
            total = float(price) * float(quantity)

            net = 0.0

            self.listmodel.append(
                [desc, unity, str("%.2f" % float(quantity)), str("%.2f" % float(price)),
                 str("%.2f" %  total)])
            for row in self.listmodel:
                # Print values of all columns
                net = net + float(row[:][-1])

            self.invoice_net_sum.set_text(str("%.2f" % net))
            tax = net * (float(settings.get_uint('tax-rate')) /100)
            self.invoice_tax_sum.set_text(str("%.2f" % tax))
            if settings.get_boolean('tax-on-invoice'):
                total = net+tax
                self.invoice_total_sum.set_text(str("%.2f" % total))

            dialog.destroy()



    def remove_cb(self, button):
        settings = Gio.Settings('com.github.maltekiefer.invoicy')
        if len(self.listmodel) != 0:
            (self.listmodel, iter) = self.selection.get_selected()
            if iter is not None:
                net = 0.0
                self.listmodel.remove(iter)
                for row in self.listmodel:
                    # Print values of all columns
                    net = net + float(row[:][-1])

                self.invoice_net_sum.set_text(str("%.2f" % net))
                tax = net * (float(settings.get_uint('tax-rate')) / 100)
                self.invoice_tax_sum.set_text(str("%.2f" % tax))
                if settings.get_boolean('tax-on-invoice'):
                    total = net + tax
                    self.invoice_total_sum.set_text(str("%.2f" % total))
