#!/usr/bin/env python3

import gi
import os.path
from os import path
from appdirs import AppDirs
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class HeaderBarWindow(Gtk.Window):

    def __init__(self):
        dirs = AppDirs("invoicy", "Malte Kiefer")
        print()
        
        if path.exists(dirs.user_config_dir+"/config.toml"):
            print("ja")
        else:
            print("nein")
            
        
        Gtk.Window.__init__(self, title="invoicy")
        self.set_border_width(10)
        self.set_default_size(600, 400)
        self.set_position(3)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "invoicy"
        self.set_titlebar(hb)
                
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        
        checkbutton = Gtk.CheckButton("Company")
        stack.add_titled(checkbutton, "check", "Company")
        
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "Customer")
        
        label2 = Gtk.Label()
        label2.set_markup("<big>A fancy label</big>")
        stack.add_titled(label2, "label2", "Invoice")

        grid = Gtk.Grid()
        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
        stack.add_titled(grid, "settings", "Settings")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(stack_switcher, False, False, 0)
        vbox.pack_start(stack, False, False, 0)


win = HeaderBarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

