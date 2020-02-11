#!/usr/bin/python3

import os
import gi
import webbrowser
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite
try:
    import constants as cn
except ImportError:
    import invoicy.constants as cn

class Invoice(Gtk.Box):
    status = False

    def __init__(self, parent):
        Gtk.Box.__init__(self, False, 0)
        self.parent = parent

        self.set_border_width(80)

        self.set_orientation(Gtk.Orientation.VERTICAL)

        title = Gtk.Label()
        title.set_markup("<big><b>Add new Invoice</b></big>")
        title.set_name('Title')
        title.set_justify(Gtk.Justification.CENTER)
        self.add(title)
