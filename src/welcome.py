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

class Welcome(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, False, 0)

        self.parent = parent

        # Create welcome widget
        self.welcome = Granite.WidgetsWelcome()
        self.welcome = self.welcome.new(cn.App.application_name, cn.App.application_description)

        # Welcome voices
        self.welcome.append("document-new", "Create Invoice", "Create a new invoice")


        self.welcome.connect("activated", self.on_welcome_activated)

        self.add(self.welcome)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            # Add invoice
            self.parent.stack.set_visible_child_name("invoice")
