#!/usr/bin/python3

import os
import gi
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite
try:
    import constants as cn
    import welcome as wl
    import invoice as inv
except ImportError:
    import invoicy.constants as cn
    import invoicy.welcome as wl
    import invoicy.invoice as inv

class Stack(Gtk.Box):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.parent = parent

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(1000)
        
        self.welcome = wl.Welcome(self)
        self.invoice = inv.Invoice(self)

        self.stack.add_titled(self.welcome, "welcome", "Welcome")
        self.stack.add_titled(self.invoice, "invoice", "Invoice")

        self.pack_start(self.stack, True, True, 0)