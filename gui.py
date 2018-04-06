import tkinter as tk
from data import *
from rocket_view import RocketView
import time
from log import Log
import numpy as np
import re


class SimGUI:


    def __init__(self):
        self.root = tk.Tk()
        self.root.config(Aspect.frame_opt())
        self.init_window()

        self.fps = 60.0
        self.t = 0.0
        self.dt = 1.0 / self.fps

        self.init_rocket_view()
        self.init_info()
        self.init_controls()
        self.init_prompter()

        self.root.mainloop()

    def init_window(self):
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()

        self.window_height = int(screen_height * Aspect.window_scale)
        self.window_width = int(screen_width * Aspect.window_scale)

        self.root.minsize(width=self.window_width, height=self.window_height)
        self.root.maxsize(width=self.window_width, height=self.window_height)

    def init_rocket_view(self):
        self.rocket_view = RocketView(self)

    def init_info(self):
        self.info_frame = tk.Frame(self.root)
        self.info_frame.config(Aspect.frame_opt())
        self.info_frame.grid(column=1,row=0, sticky=Aspect.def_sticky)
        self.info_frame.grid_columnconfigure(0, minsize=int(self.window_width / 2))

        self.info_title = tk.Label(self.info_frame, text='Simulation & Rocket Info')
        self.info_title.config(Aspect.frame_opt())
        self.info_title.config(justify=tk.CENTER)
        self.info_title.grid(row=0, sticky=tk.W + tk.E)
       
        self.play_simu = tk.Button(self.info_frame, text='Start', command=self.simulate)
        self.play_simu.config(Aspect.button_opt())
        self.play_simu.grid(column=0, row=1, sticky=Aspect.def_sticky)

    def init_controls(self):
        self.control_frame = tk.Frame(self.root)
        self.control_frame.config(Aspect.frame_opt())
        self.control_frame.grid(column=1,row=1, sticky=Aspect.def_sticky)
        self.control_frame.grid_columnconfigure(0, minsize=int(self.window_width / 2))

        self.control_title = tk.Label(self.control_frame, text='Controls')
        self.control_title.config(Aspect.frame_opt())
        self.control_title.config(justify=tk.CENTER)
        self.control_title.grid(row=0, sticky=tk.W + tk.E)

    def init_prompter(self):
        self.prompter_frame = tk.Frame(self.root)
        self.prompter_frame.config(Aspect.frame_opt())
        self.prompter_frame.grid(column=1,row=3, sticky=Aspect.def_sticky)
        # self.prompter_frame.grid_columnconfigure(0, minsize=int(self.window_width / 2))

        self.prompter_frame_it = tk.Frame(self.prompter_frame)
        self.prompter_frame_it.config(Aspect.frame_opt())
        self.prompter_frame_it.grid(column=1,row=0, sticky=Aspect.def_sticky)
        # self.prompter_frame_it.grid_columnconfigure(0, minsize=int(self.window_width / 4))
        self.prompter_it = Prompter(self.prompter_frame_it, name='IT')

        self.prompter_frame_sim = tk.Frame(self.prompter_frame)
        self.prompter_frame_sim.config(Aspect.frame_opt())
        self.prompter_frame_sim.grid(column=0, row=0, sticky=Aspect.def_sticky)
        # self.prompter_frame_sim.grid_columnconfigure(0, minsize=int(self.window_width / 4))
        self.prompter_sim = Prompter(self.prompter_frame_sim, name='Simulation')

    def simulate(self):
        while self.t < Simu.max_sim_duration:
            self.t = self.t + self.dt
            theta = 30.0 * np.sin(self.t)
            self.rocket_view.set_angle(theta)
            self.prompter_it.feed('Time {}:'.format(self.t))


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

        self.text = list()
        self.label = tk.Label(self.frame)
        self.label.config(justify=tk.LEFT)
        self.label.config(Aspect.frame_opt())
        self.label.config(relief=tk.SUNKEN)
        self.feed(Prompter.V_LIM * Prompter.H_LIM * ' ')
        self.feed('{} Prompter initialization.'.format(self.name))
        self.label.grid(row=1, column=0, columnspan=5)

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
        self.text += table
        n = len(self.text)
        if n > Prompter.V_LIM:
            self.text = self.text[n - Prompter.V_LIM:]
        self.refresh()

    def refresh(self):
        self.label.config(text=self.get_text())

    def get_tag_txt(self):
        txt = ''
        # type "%H:%M:%S" for full time.
        time_flag = time.strftime("%H:%M", time.gmtime())
        txt += '[{}]'.format(time_flag)
        return txt