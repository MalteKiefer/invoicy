#!/usr/bin/python3


import gi
import gettext
_ = gettext.gettext

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite, GObject
try:
    import constants as cn
    import window as wn
except ImportError:
    import invoicy.constants as cn
    import invoicy.window as wn

class Application(Granite.Application):

    def do_activate(self):
        self.win = wn.Window()
        self.win.set_default_size(800, 600)
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.show_all()
        self.win.hbar.back.hide()

        Gtk.main()

app = Application()

stylesheet = """
    @define-color colorPrimary """+cn.Colors.primary_color+""";
    @define-color textColorPrimary """+cn.Colors.primary_text_color+""";
    @define-color textColorPrimaryShadow """+cn.Colors.primary_text_shadow_color+""";
""";

style_provider = Gtk.CssProvider()
style_provider.load_from_data(bytes(stylesheet.encode()))
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

app.run("")
