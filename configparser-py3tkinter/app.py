"""
configparser-py3tkinter
-----------------

Python 3 Tkinter GUI
"""

import datetime
import tkinter

# All translations provided for illustrative purposes only.
 # english
from .translation import _
from .main_frame import MainFrame
from .menu_bar import MenuBar
from .tool_bar import ToolBar
from .status_bar import StatusBar
from .navigation_bar import NavigationBar


class Application(tkinter.Tk):
    "Create top-level Tkinter widget containing all other widgets."

    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)
        self.wm_title('configparser Tkinter GUI')
        self.wm_geometry('640x480')

# Status bar selection == 'y'
        self.statusbar = StatusBar(self)
        self.statusbar.pack(side='bottom', fill='x')
        self.bind_all('<Enter>', lambda e: self.statusbar.set_text(0,
                      'Mouse: 1'))
        self.bind_all('<Leave>', lambda e: self.statusbar.set_text(0,
                      'Mouse: 0'))
        self.bind_all('<Button-1>', lambda e: self.statusbar.set_text(1,
                      'Clicked at x = ' + str(e.x) + ' y = ' + str(e.y)))
        self.start_time = datetime.datetime.now()
        self.uptime()


# Navigation selection == 'y'
        self.navigationbar = NavigationBar(self)
        self.navigationbar.pack(side='left', fill='y')


# Tool bar selection == 'y'
        self.toolbar = ToolBar(self)
        self.toolbar.pack(side='top', fill='x')


        self.mainframe = MainFrame(self)
        self.mainframe.pack(side='right', fill='y')

# Status bar selection == 'y'
    def uptime(self):
        _upseconds = str(int(round((datetime.datetime.now() - self.start_time).total_seconds())))
        self.statusbar.set_text(2, _('Uptime') + ': ' + _upseconds)
        self.after(1000, self.uptime)
