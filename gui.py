from log import Log
from data import *
from rocket_view import RocketView
from prompter import Prompter
import tkinter as tk
import time
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
        self.prompter_it = Prompter(self.prompter_frame_it, name='IT')

        self.prompter_frame_sim = tk.Frame(self.prompter_frame)
        self.prompter_frame_sim.config(Aspect.frame_opt())
        self.prompter_frame_sim.grid(column=0, row=0, sticky=Aspect.def_sticky)
        self.prompter_sim = Prompter(self.prompter_frame_sim, name='Simulation')

    def simulate(self):
        t0 = self.t
        while self.t < Simu.max_sim_duration + t0:
            self.t = self.t + self.dt
            theta = 30.0 * np.sin(self.t)
            self.rocket_view.set_angle(theta)
            self.prompter_it.feed('Time {}:'.format(self.t))
            self.update_all()

    def update_all(self):
        pass
