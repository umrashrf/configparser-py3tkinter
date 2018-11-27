import tkinter
import tkinter.ttk as ttk

from .translation import _


class ToolBar(ttk.Frame):
    "Sample toolbar provided by cookiecutter switch."

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.buttons = []
        self.config(border=1, relief=tkinter.GROOVE)
        for i in range(1, 5):
            _button_text = _('Tool ') + str(i)
            self.buttons.append(ttk.Button(self, text=_button_text,
                                           command=lambda i=i:
                                           self.run_tool(i)))
            self.buttons[i - 1].pack(side=tkinter.LEFT, fill=tkinter.X)
        self.pack()

    def run_tool(self, number):
        "Sample function provided to show how a toolbar command may be used."

        print(_('Toolbar button'), number, _('pressed'))
