import sys
import tkinter

from .translation import _
from .popup_dialog import PopupDialog


class MenuBar(tkinter.Menu):
    "Menu bar appearing with expected components."

    def __init__(self, parent):
        tkinter.Menu.__init__(self, parent)

        filemenu = tkinter.Menu(self, tearoff=False)
        filemenu.add_command(label=_('New'), command=self.new_dialog)
        filemenu.add_command(label=_('Open'), command=self.open_dialog)
        filemenu.add_separator()
        filemenu.add_command(label=_('Exit'), underline=1,
                             command=self.quit)

        helpmenu = tkinter.Menu(self, tearoff=False)
        helpmenu.add_command(label=_('Help'), command=lambda:
                             self.help_dialog(None), accelerator="F1")
        helpmenu.add_command(label=_('About'), command=self.about_dialog)
        self.bind_all('<F1>', self.help_dialog)

        self.add_cascade(label=_('File'), underline=0, menu=filemenu)
        self.add_cascade(label=_('Help'), underline=0, menu=helpmenu)

    def quit(self):
        "Ends toplevel execution."

        sys.exit(0)

    def help_dialog(self, event):
        "Dialog cataloging results achievable, and provided means available."

        _description = _('Help not yet created.')
        PopupDialog(self, 'configparser Tkinter GUI', _description)

    def about_dialog(self):
        "Dialog concerning information about entities responsible for program."

        _description = 'Python 3 Tkinter GUI'
        if _description == '':
            _description = _('No description available')
        _description += '\n'
        _description += '\n' + _('Author') + ': Umair Ashraf'
        _description += '\n' + _('Email') + ': umrashrf@gmail.com'
        _description += '\n' + _('Version') + ': 0.0.1'
        _description += '\n' + _('GitHub Package') + \
                        ': configparser-py3tkinter'
        PopupDialog(self, _('About') + ' configparser Tkinter GUI',
                    _description)

    def new_dialog(self):
        "Non-functional dialog indicating successful navigation."

        PopupDialog(self, _('New button pressed'), _('Not yet implemented'))

    def open_dialog(self):
        "Standard askopenfilename() invocation and result handling."

        _name = tkinter.filedialog.askopenfilename()
        if isinstance(_name, str):
            print(_('File selected for open: ') + _name)
        else:
            print(_('No file selected'))
