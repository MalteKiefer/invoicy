#!/usr/bin/python3

import os
import gi
import gettext
import pandas
_ = gettext.gettext
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite, Gio
from datetime import timedelta, date
from appdirs import *
from pandas import DataFrame

try:
    import constants as cn
except ImportError:
    import invoicy.constants as cn

class Customer(Gtk.Box):

    def __init__(self, parent):

        Gtk.Box.__init__(self, False, 0)
        self.parent = parent
        self.set_border_width(10)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        grid_customer = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid_customer.set_halign(Gtk.Align.CENTER)
        grid_customer.props.margin_left = 20
        grid_customer.props.margin_right = 20
        grid_customer.props.margin_top = 20
        grid_customer.props.margin_bottom = 20

        customer_label = Gtk.Label()
        customer_label.set_markup(_("<big><b>Customer</b></big>"))
        customername_label = Gtk.Label(_("Company"))
        customername_entry = Gtk.Entry()

        customercontact_label = Gtk.Label(_("Contact"))
        customercontact_entry = Gtk.Entry()

        customerstreet_label = Gtk.Label(_("Street"))
        customerstreet_entry = Gtk.Entry()

        customerzip_label = Gtk.Label(_("ZIP"))
        customerzip_entry = Gtk.Entry()

        customercity_label = Gtk.Label(_("City"))
        customercity_entry = Gtk.Entry()

        customercountry_label = Gtk.Label(_("Country"))
        customercountry_entry = Gtk.Entry()

        customervat_label = Gtk.Label(_("VAT"))
        customervat_entry = Gtk.Entry()

        grid_customer.attach(customer_label, 0, 1, 2, 1)
        grid_customer.attach(customername_label, 0, 2, 1, 1)
        grid_customer.attach(customername_entry, 1, 2, 1, 1)
        grid_customer.attach(customercontact_label, 0, 3, 1, 1)
        grid_customer.attach(customercontact_entry, 1, 3, 1, 1)
        grid_customer.attach(customerstreet_label, 0, 4, 1, 1)
        grid_customer.attach(customerstreet_entry, 1, 4, 1, 1)
        grid_customer.attach(customerzip_label, 0, 5, 1, 1)
        grid_customer.attach(customerzip_entry, 1, 5, 1, 1)
        grid_customer.attach(customercity_label, 0, 6, 1, 1)
        grid_customer.attach(customercity_entry, 1, 6, 1, 1)
        grid_customer.attach(customercountry_label, 0, 7, 1, 1)
        grid_customer.attach(customercountry_entry, 1, 7, 1, 1)
        grid_customer.attach(customervat_label, 0, 8, 1, 1)
        grid_customer.attach(customervat_entry, 1, 8, 1, 1)

        self.add(grid_customer)

        btn_add_customer = Gtk.Button.new_with_label("Next")
        btn_add_customer.connect("clicked", self.btn_add_customer_clicked)
        btn_cancel = Gtk.Button.new_with_label("Cancel")
        btn_cancel.connect("clicked", self.btn_cancel_clicked)

        btn_box = Gtk.Box(spacing=6)
        self.add(btn_box)
        btn_box.pack_end(btn_add_customer, False, True, 0)
        btn_box.pack_end(btn_cancel, False, True, 0)


    def btn_add_customer_clicked(self, widget):

        self.parent.stack.set_visible_child_name("invoice")

    def btn_cancel_clicked(self, button):
        self.parent.stack.set_visible_child_name("welcome")
