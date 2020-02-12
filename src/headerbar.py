import gi
import gettext
_ = gettext.gettext

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio
try:
    import constants as cn
    import dialogs as di
except ImportError:
    import invoicy.constants as cn
    import invoicy.dialogs as di

class Headerbar(Gtk.HeaderBar):

    def __init__(self, parent):

        Gtk.HeaderBar.__init__(self)
        self.parent = parent

        self.set_show_close_button(True)
        self.props.title = cn.App.application_name

        # menu button
        self.menubutton = Gtk.Button(None,image=Gtk.Image.new_from_gicon(Gio.ThemedIcon(name="open-menu"), Gtk.IconSize.LARGE_TOOLBAR))
        self.menubutton.connect("clicked", self.on_menu_clicked )
        self.pack_end(self.menubutton)

        self.settings_popover = Gtk.Popover()
        self.settings_popover_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.settings = Gtk.ModelButton(_("Settings"))
        self.settings.connect("clicked", di.Dialogs.settingsdialog)
        self.settings_popover_vbox.pack_start(self.settings, False, True, 2)
        self.company = Gtk.ModelButton(_("Company"))
        self.company.connect("clicked", di.Dialogs.companydialog)
        self.settings_popover_vbox.pack_start(self.company, False, True, 2)
        self.about = Gtk.ModelButton(_("About"))
        self.about.connect("clicked", di.Dialogs.aboutdialog)
        self.settings_popover_vbox.pack_start(self.about, False, True, 2)
        self.settings_popover.add(self.settings_popover_vbox)
        self.settings_popover.set_position(Gtk.PositionType.BOTTOM)

        # new invoice
        self.add_invoice = Gtk.Button(None,image=Gtk.Image.new_from_gicon(Gio.ThemedIcon(name="document-new"), Gtk.IconSize.LARGE_TOOLBAR))
        self.add_invoice.connect("clicked", self.on_new_invoice_clicked )
        self.pack_start(self.add_invoice)


    def on_menu_clicked(self, button):
        self.settings_popover.set_relative_to(button)
        self.settings_popover.show_all()
        self.settings_popover.popup()

    def on_new_invoice_clicked(self, widget):
        self.parent.stack.stack.set_visible_child_name("invoice")
