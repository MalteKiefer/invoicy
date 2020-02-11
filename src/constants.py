#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class App:
    application_id = "com.github.maltekiefer.invoicy"
    application_name = "invoicy"
    application_description = "Create simple and clean invoices at elementaryOS"
    application_version ="1.0.0"
    main_url = "https://github.com/maltekiefer/invoicy"
    bug_url = "https://github.com/maltekiefer/invoicy/issues/labels/bug"
    help_url = "https://github.com/maltekiefer/invoicy/issues"
    about_authors = ["Malte Kiefer <malte.kiefer@mailgermania.de>"]
    about_comments = application_description
    about_license_type = Gtk.License.MIT_X11

class Colors:
    primary_color = "#6699cc"
    primary_text_color = "#172d4f"
    primary_text_shadow_color = "#bdbdbd"