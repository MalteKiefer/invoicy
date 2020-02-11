#!/usr/bin/python3

import os
import gi
import gettext
_ = gettext.gettext

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf
try:
    import constants as cn
except ImportError:
    import invoicy.constants as cn

class Dialogs(Gtk.Box):

    def settingsdialog (self):

        def set_active(self, widget):
            if financetax_switch.get_active():
                financetaxrate_entry.set_sensitive(True)
            else:
                financetaxrate_entry.set_sensitive(False)

        settings = Gio.Settings('com.github.maltekiefer.invoicy')

        dialog = Gtk.Dialog()

        dialog.set_default_size(300, 300)
        dialog.set_modal(True)
        dialog.add_button(button_text="Cancel", response_id=Gtk.ResponseType.CANCEL)
        dialog.add_button(button_text="Save", response_id=Gtk.ResponseType.OK)

        grid_finance = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid_finance.props.margin_left = 20
        grid_finance.props.margin_right = 20
        grid_finance.props.margin_top = 20
        grid_finance.props.margin_bottom = 20

        settings_label = Gtk.Label()
        settings_label.set_markup(_("<big><b>Settings</b></big>"))

        financecurrency_label = Gtk.Label(_("Currency Symbole"), xalign=0)
        financecurrency_entry = Gtk.Entry()
        financecurrency_entry.set_text(settings.get_string('currency-symbole'))

        financecurrencyposition_label = Gtk.Label(_("Currency Symbole Position"), xalign=0)
        financecurrencyposition_combo = Gtk.ComboBoxText()
        financecurrencyposition_combo.insert(0, "0", _("Left"))
        financecurrencyposition_combo.insert(1, "1", _("Right"))
        financecurrencyposition_combo.set_active(settings.get_uint('currency-symbole-position'))
        financetax_label = Gtk.Label(_("Show taxes on the invoice?"), xalign=0)
        financetax_switch = Gtk.Switch(halign=Gtk.Align.END)
        financetax_switch.set_active(settings.get_boolean('tax-on-invoice'))
        financetaxrate_label = Gtk.Label(_("Tax rate (only numbers)"), xalign=0)
        financetaxrate_entry = Gtk.Entry()
        financetaxrate_entry.set_text(str(settings.get_uint('tax-rate')))
        financetaxrate_entry.set_sensitive(False)
        financetax_switch.connect("notify::active", set_active)

        if settings.get_boolean('tax-on-invoice'):
            financetaxrate_entry.set_sensitive(True)

        grid_finance.attach(settings_label, 0, 1, 2, 1)
        grid_finance.attach(financecurrency_label, 0, 2, 1, 1)
        grid_finance.attach(financecurrency_entry, 1, 2, 1, 1)
        grid_finance.attach(financecurrencyposition_label, 0, 3, 1, 1)
        grid_finance.attach(financecurrencyposition_combo, 1, 3, 1, 1)
        grid_finance.attach(financetax_label, 0, 4, 1, 1)
        grid_finance.attach(financetax_switch, 1, 4, 1, 1)
        grid_finance.attach(financetaxrate_label, 0, 5, 1, 1)
        grid_finance.attach(financetaxrate_entry, 1, 5, 1, 1)
        box = dialog.get_content_area()

        box.add(grid_finance)

        dialog.show_all()

        return_code = dialog.run ()
        financecurrency = financecurrency_entry.get_text()
        financecurrencyposition = financecurrencyposition_combo.get_active()
        financetax = financetax_switch.get_active()
        financetaxrate = int(financetaxrate_entry.get_text())
        dialog.destroy()

        if return_code == Gtk.ResponseType.OK:
            settings.set_string ('currency-symbole', financecurrency)
            settings.set_uint ('currency-symbole-position', financecurrencyposition)
            settings.set_boolean ('tax-on-invoice', financetax)
            settings.set_uint('tax-rate', financetaxrate)


    def companydialog(self):
        settings = Gio.Settings('com.github.maltekiefer.invoicy')

        dialog = Gtk.Dialog()

        dialog.set_default_size(300, 300)
        dialog.set_modal(True)
        dialog.add_button(button_text="Cancel",
                          response_id=Gtk.ResponseType.CANCEL)
        dialog.add_button(button_text="Save", response_id=Gtk.ResponseType.OK)

        grid_company = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid_company.props.margin_left = 20
        grid_company.props.margin_right = 20
        grid_company.props.margin_top = 20
        grid_company.props.margin_bottom = 20

        company_label = Gtk.Label()
        company_label.set_markup(_("<big><b>Company</b></big>"))
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

        grid_company.attach(company_label, 0, 1, 2, 1)
        grid_company.attach(companyname_label, 0, 2, 1, 1)
        grid_company.attach(companyname_entry, 1, 2, 1, 1)
        grid_company.attach(companycontact_label, 0, 3, 1, 1)
        grid_company.attach(companycontact_entry, 1, 3, 1, 1)
        grid_company.attach(companystreet_label, 0, 4, 1, 1)
        grid_company.attach(companystreet_entry, 1, 4, 1, 1)
        grid_company.attach(companyzip_label, 0, 4, 1, 1)
        grid_company.attach(companyzip_entry, 1, 4, 1, 1)
        grid_company.attach(companycity_label, 0, 5, 1, 1)
        grid_company.attach(companycity_entry, 1, 5, 1, 1)
        grid_company.attach(companycountry_label, 0, 6, 1, 1)
        grid_company.attach(companycountry_entry, 1, 6, 1, 1)
        grid_company.attach(companyvat_label, 0, 7, 1, 1)
        grid_company.attach(companyvat_entry, 1, 7, 1, 1)
        box = dialog.get_content_area()

        box.add(grid_company)

        dialog.show_all()

        return_code = dialog.run ()
        compnanyname = companyname_entry.get_text()
        companycontact = companycontact_entry.get_text()
        companystreet = companystreet_entry.get_text()
        companyzip = companyzip_entry.get_text()
        companycity = companycity_entry.get_text()
        companycountry = companycountry_entry.get_text()
        companyvat_entry = companyvat_entry.get_text()
        dialog.destroy()

        if return_code == Gtk.ResponseType.OK:
            settings.set_string('company-name', compnanyname)
            settings.set_string('company-contact', companycontact)
            settings.set_string('company-street', companystreet)
            settings.set_string('company-zip', companyzip)
            settings.set_string('company-city', companycity)
            settings.set_string('company-country', companycountry)
            settings.set_string('company-vat', companyvat_entry)

        return None

    def aboutdialog(self):
        about_dialog = Gtk.AboutDialog()

        about_dialog.set_destroy_with_parent(True)
        about_dialog.set_program_name(cn.App.application_name)
        about_dialog.set_version(cn.App.application_version)
        about_dialog.set_license('''
        MIT License

        Copyright (c) 2020 Malte Kiefer

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        ''')
        about_dialog.set_authors(cn.App.about_authors)
        about_dialog.set_website(cn.App.main_url)
        about_dialog.set_comments(cn.App.application_description)
        about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file('src/assets/invoice.png'))

        about_dialog.run()
        about_dialog.destroy()
