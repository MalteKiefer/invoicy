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

        grid_finance.attach(financecurrency_label, 0, 1, 1, 1)
        grid_finance.attach(financecurrency_entry, 1, 1, 1, 1)
        grid_finance.attach(financecurrencyposition_label, 0, 2, 1, 1)
        grid_finance.attach(financecurrencyposition_combo, 1, 2, 1, 1)
        grid_finance.attach(financetax_label, 0, 3, 1, 1)
        grid_finance.attach(financetax_switch, 1, 3, 1, 1)
        box = dialog.get_content_area()

        box.add(grid_finance)  

        dialog.show_all()

        return_code = dialog.run ()
        financecurrency = financecurrency_entry.get_text()
        financecurrencyposition = financecurrencyposition_combo.get_active()
        financetax = financetax_switch.get_active()
        dialog.destroy()

        if return_code == Gtk.ResponseType.OK:
            settings.set_string ('currency-symbole', financecurrency)
            settings.set_uint ('currency-symbole-position', financecurrencyposition)
            settings.set_boolean ('tax-on-invoice', financetax)

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
        about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file('assets/invoice.png'))

        about_dialog.run()
        about_dialog.destroy() 