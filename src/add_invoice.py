#!/usr/bin/python3

import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite, Gio
from datetime import timedelta, date

try:
    import constants as cn
except ImportError:
    import invoicy.constants as cn

class Invoice(Gtk.Box):
    status = False

    def __init__(self, parent):

        def calc_total(self):
            entity = float(pos_3_entry.get_text())
            price = float(pos_4_entry.get_text())
            pos_5_entry.set_text(str(entity * price))

        settings = Gio.Settings('com.github.maltekiefer.invoicy')

        Gtk.Box.__init__(self, False, 0)
        self.parent = parent

        self.set_border_width(10)

        self.set_orientation(Gtk.Orientation.VERTICAL)

        due_date = date.today() + timedelta(
            days=settings.get_uint('invoice-due-days'))

        btn_create_invoice = Gtk.Button.new_with_label("Create Invoice")
        btn_cancel = Gtk.Button.new_with_label("Cancel")
        btn_cancel.connect("clicked", self.btn_cancel_clicked)

        title = Gtk.Label()
        title.set_markup("<big><b>New Invoice</b></big>")

        cus_store_label = Gtk.Label("Customer")
        cus_store = Gtk.ComboBoxText()
        cus_store.insert(0, "0", "Johne Doe")
        cus_store.insert(1, "1", "Jane Doe")

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

        pos_1_label = Gtk.Label("Description")
        pos_2_label = Gtk.Label("Quantity")
        pos_3_label = Gtk.Label("Entity")
        pos_4_label = Gtk.Label("Price")
        pos_5_label = Gtk.Label("Total")

        pos_1_entry = Gtk.Entry()
        pos_2_entry = Gtk.Entry()
        pos_3_entry = Gtk.Entry()
        pos_3_entry.connect("changed", calc_total)
        pos_4_entry = Gtk.Entry()
        pos_4_entry.connect("changed", calc_total)
        pos_5_entry = Gtk.Entry()
        pos_5_entry.set_sensitive(False)

        grid_invoice = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid_invoice.props.margin_left = 20
        grid_invoice.props.margin_right = 20
        grid_invoice.props.margin_top = 20
        grid_invoice.props.margin_bottom = 20

        grid_invoice.attach(title, 0, 1, 5, 1)
        grid_invoice.attach(cus_store_label, 0, 2, 1, 1)
        grid_invoice.attach(cus_store, 1, 2, 1, 1)

        grid_invoice.attach(invoice_date_label, 3, 2, 1, 1)
        grid_invoice.attach(invoice_date_entry, 4, 2, 1, 1)

        grid_invoice.attach(btn_create_invoice, 5, 2, 1, 1)

        grid_invoice.attach(invoice_number_label, 0, 3, 1, 1)
        grid_invoice.attach(invoice_number_entry, 1, 3, 1, 1)

        grid_invoice.attach(invoice_due_label, 3, 3, 1, 1)
        grid_invoice.attach(invoice_due_entry, 4, 3, 1, 1)

        grid_invoice.attach(btn_cancel, 5, 3, 1, 1)

        self.add(grid_invoice)

        grid_positions = Gtk.Grid(column_spacing=20,
                                  row_spacing=20,
                                  margin=24,
                                  hexpand=True,
                                  halign=True)

        grid_positions.attach(pos_1_label, 1, 1, 1, 1)
        grid_positions.attach(pos_2_label, 2, 1, 1, 1)
        grid_positions.attach(pos_3_label, 3, 1, 1, 1)
        grid_positions.attach(pos_4_label, 4, 1, 1, 1)
        grid_positions.attach(pos_5_label, 5, 1, 1, 1)

        grid_positions.attach(pos_1_entry, 1, 2, 1, 1)
        grid_positions.attach(pos_2_entry, 2, 2, 1, 1)
        grid_positions.attach(pos_3_entry, 3, 2, 1, 1)
        grid_positions.attach(pos_4_entry, 4, 2, 1, 1)
        grid_positions.attach(pos_5_entry, 5, 2, 1, 1)

        self.add(grid_positions)



    def btn_cancel_clicked(self, button):
        self.parent.stack.set_visible_child_name("welcome")
