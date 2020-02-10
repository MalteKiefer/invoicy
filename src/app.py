#
# Copyright (c) 2020 Kiefer Networks (https://kiefer-networks.de)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#
# Authored by: Malte Kiefer <malte.kiefer@kiefer-networks.de>
#

import gi
import gettext
_ = gettext.gettext

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk, Gio, GLib

class Invoicy(Gtk.Window):

    def settingsdialog (self, widget):

        settings = Gio.Settings('com.github.maltekiefer.invoicy')

        dialog = Gtk.Dialog()

        dialog.set_default_size(300, 300)
        dialog.set_transient_for(self)
        dialog.set_modal(True)
        dialog.add_button(button_text="Cancel", response_id=Gtk.ResponseType.CANCEL)
        dialog.add_button(button_text="Save", response_id=Gtk.ResponseType.OK)

        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid.props.margin_left = 20
        grid.props.margin_right = 20
        grid.props.margin_top = 20
        grid.props.margin_bottom = 20

        header = Gtk.Label()
        header.set_markup(_("<big><b>Settings</b></big>"))
        header_company = Gtk.Label()
        header_company.set_markup(_("<b>Company</b>"))
        finance_company = Gtk.Label()
        finance_company.set_markup(_("<b>Finance</b>"))

        companyname_label = Gtk.Label(_("Company"))
        companyname_entry = Gtk.Entry()
        companyname_entry.set_text(settings.get_string('company-name'))

        companycontact_label = Gtk.Label(_("Contact"))
        companycontact_entry = Gtk.Entry()
        companycontact_entry.set_text(settings.get_string('company-contact'))

        companystreet_label = Gtk.Label(_("Street"))
        companystreet_entry = Gtk.Entry()
        companystreet_entry.set_text(settings.get_string('company-street'))

        companyzip_label = Gtk.Label(_("ZIP"))
        companyzip_entry = Gtk.Entry()
        companyzip_entry.set_text(settings.get_string('company-zip'))

        companycity_label = Gtk.Label(_("City"))
        companycity_entry = Gtk.Entry()
        companycity_entry.set_text(settings.get_string('company-city'))

        companycountry_label = Gtk.Label(_("Country"))
        companycountry_entry = Gtk.Entry()
        companycountry_entry.set_text(settings.get_string('company-country'))

        companyvat_label = Gtk.Label(_("VAT"))
        companyvat_entry = Gtk.Entry()
        companyvat_entry.set_text(settings.get_string('company-vat'))

        financecurrency_label = Gtk.Label(_("Currency Symbole"))
        financecurrency_entry = Gtk.Entry()
        financecurrency_entry.set_text(settings.get_string('currency-symbole'))

        financecurrencyposition_label = Gtk.Label(_("Currency Symbole Position"))
        financecurrencyposition_combo = Gtk.ComboBoxText()
        financecurrencyposition_combo.insert(0, "0", _("Left"))
        financecurrencyposition_combo.insert(1, "1", _("Right"))
        financecurrencyposition_combo.set_active(settings.get_int('currency-symbole-position'))

        grid.add(header)
        grid.attach(header_company, 0, 1, 2, 1)

        grid.attach(companyname_label, 0, 2, 1, 1)
        grid.attach(companyname_entry, 1, 2, 1, 1)
        grid.attach(companycontact_label, 0, 3, 1, 1)
        grid.attach(companycontact_entry, 1, 3, 1, 1)
        grid.attach(companystreet_label, 0, 4, 1, 1)
        grid.attach(companystreet_entry, 1, 4, 1, 1)
        grid.attach(companyzip_label, 0, 5, 1, 1)
        grid.attach(companyzip_entry, 1, 5, 1, 1)
        grid.attach(companycity_label, 0, 6, 1, 1)
        grid.attach(companycity_entry, 1, 6, 1, 1)
        grid.attach(companycountry_label, 0, 7, 1, 1)
        grid.attach(companycountry_entry, 1, 7, 1, 1)
        grid.attach(companyvat_label, 0, 8, 1, 1)
        grid.attach(companyvat_entry, 1, 8, 1, 1)

        grid.attach(finance_company, 0, 9, 2, 1)
        grid.attach(financecurrency_label, 0, 10, 1, 1)
        grid.attach(financecurrency_entry, 1, 10, 1, 1)
        grid.attach(financecurrencyposition_label, 0, 11, 1, 1)
        grid.attach(financecurrencyposition_combo, 1, 11, 1, 1)

        box = dialog.get_content_area()
        box.add(grid)

        dialog.show_all()

        return_code = dialog.run ()
        compnanyname = companyname_entry.get_text()
        companycontact = companycontact_entry.get_text()
        companystreet = companystreet_entry.get_text()
        companyzip = companyzip_entry.get_text()
        companycity = companycity_entry.get_text()
        companycountry = companycountry_entry.get_text()
        companyvat_entry = companyvat_entry.get_text()
        financecurrency = financecurrency_entry.get_text()
        financecurrencyposition = financecurrencyposition_combo.get_active()
        dialog.destroy()

        if return_code == Gtk.ResponseType.OK:
            settings.set_string ('company-name', compnanyname)
            settings.set_string ('company-contact', companycontact)
            settings.set_string ('company-street', companystreet)
            settings.set_string ('company-zip', companyzip)
            settings.set_string ('company-city', companycity)
            settings.set_string ('company-country', companycountry)
            settings.set_string ('company-vat', companyvat_entry)
            settings.set_string ('currency-symbole', financecurrency)
            settings.set_int ('currency-symbole-position', financecurrencyposition)
            
        return None 

    def __init__(self):
        
        Gtk.Window.__init__(self, title="Invoicy")
        self.set_border_width = 10
        self.set_default_size(800, 600)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Invoicy"
        self.set_titlebar(header_bar)

        newbutton = Gtk.Button(None,image=Gtk.Image.new_from_gicon(Gio.ThemedIcon(name="document-new"), Gtk.IconSize.LARGE_TOOLBAR))
        header_bar.pack_start(newbutton)

        menubutton = Gtk.Button(None,image=Gtk.Image.new_from_gicon(Gio.ThemedIcon(name="open-menu"), Gtk.IconSize.LARGE_TOOLBAR))
        menubutton.connect("clicked", self.settingsdialog)
        header_bar.pack_end(menubutton)

        page1 = Gtk.Box()
        page1.set_border_width(10)
        page1.add(Gtk.Label('Default Page!'))

        self.add(page1)

win = Invoicy()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()