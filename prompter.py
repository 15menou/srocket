from data import Aspect
from log import Log
import tkinter as tk
import re
import time

class Prompter:

    H_LIM = 30  # Number of character in the same row. Does not include tag.
    V_LIM = 10  # Number of rows

    def __init__(self, init_frame, name=None):
        self.frame = init_frame
        if name is None:
            name = 'Prompter'
        self.name = name

        self.title = tk.Label(self.frame, text=self.name.strip())
        self.title.config(Aspect.frame_opt())
        self.title.config(justify=tk.CENTER)
        self.title.grid(row=0, column=0, sticky=Aspect.def_sticky)

        self.history = list()

        self.text = list()
        self.label = tk.Label(self.frame)
        self.label.config(justify=tk.LEFT)
        self.label.config(Aspect.frame_opt())
        self.label.config(relief=tk.SUNKEN)
        self.feed(Prompter.V_LIM * Prompter.H_LIM * ' ')
        self.feed('{} Prompter initialization.'.format(self.name))
        self.label.grid(row=1, column=0, columnspan=5)
        Log.comment("Prompter '{}' initialized.".format(self.name))

    def get_text(self):
        return " \n".join(self.text)

    def feed(self, txt):
        tag_txt = self.get_tag_txt()
        empty_tag = int(len(tag_txt) * 1.7) * ' '
        txt = re.sub('\n', ' ', txt)

        def cut(s):
            if len(s) < Prompter.H_LIM:
                return [s]
            else:
                first_part = s[:Prompter.H_LIM]
                second_part = s[Prompter.H_LIM:]
                if not len(first_part) == 0 and not len(second_part) == 0:
                    if not(first_part[-1] == ' ' or second_part[0] == ' '):
                        first_part += '-'
                return [first_part] + cut(second_part)

        table = cut(txt)
        for k in range(len(table)):
            if k == 0:
                table[k] = tag_txt + ' ' + table[k]
            else:
                table[k] = empty_tag + ' ' + table[k]
        self.add_content(table)
        self.reshape()
        self.refresh()

    def add_content(self, tab):
        self.text += tab
        self.history += tab

    def reshape(self):
        n = len(self.text)
        if n > Prompter.V_LIM:
            self.text = self.text[n - Prompter.V_LIM:]

    def refresh(self):
        self.label.config(text=self.get_text())

    def get_tag_txt(self):
        txt = ''
        # type "%H:%M:%S" for full time.
        time_flag = time.strftime("%H:%M", time.gmtime())
        txt += '[{}]'.format(time_flag)
        return txt