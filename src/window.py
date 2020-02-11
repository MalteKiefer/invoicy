import gi
from datetime import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
try:
    import constants as cn
    import headerbar as hb
    import stack as sk
except ImportError:
    import invoicy.constants as cn
    import invoicy.headerbar as hb
    import invoicy.stack as sk

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title=cn.App.application_name)

        self.hbar = hb.Headerbar(self)
        self.set_titlebar(self.hbar)

        self.stack = sk.Stack(self)
        self.add(self.stack)

