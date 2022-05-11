import gi
import subprocess as sp
import os
gi.require_version("Gtk", "3.0")
gi.require_version("Notify", "0.7")
from gi.repository import Gtk
from gi.repository import Notify

import editWindow
import mainWindow

mainWindow = mainWindow.mainWindow()
mainWindow.connect("destroy", Gtk.main_quit)
mainWindow.show_all()
Gtk.main()
