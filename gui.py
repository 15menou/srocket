import tkinter as tk
from data import *
from rocket_view import RocketView
import time
from log import Log
import numpy as np


class SimGUI:


    def __init__(self):
        self.root = tk.Tk()
        self.root.config(Aspect.frame_opt())
        self.window_height = None
        self.window_width = None
        self.init_window()

        self.go_stop = 'stop'
        self.fps = 60.0
        self.dt = 1.0 / self.fps

        self.init_rocket_view()
        self.init_info()
        self.init_controls()

        self.root.mainloop()

    def init_window(self):
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()

        self.window_height = int(screen_height * Aspect.window_scale)
        self.window_width = int(screen_width * Aspect.window_scale)

        self.root.minsize(width=self.window_width, height=self.window_height)
        self.root.maxsize(width=self.window_width, height=self.window_height)

    def init_rocket_view(self):
        # self.rocket_view_frame = tk.Frame(self.root)
        # self.rocket_view_frame.config(Aspect.frame_opt())
        # self.rocket_view_frame.grid(column=0,row=0, sticky=Aspect.def_sticky)
        # self.rocket_view_frame.grid_columnconfigure(0, minsize=int(self.window_width / 2))
        self.rocket_view = RocketView(self)

    def init_info(self):
        self.info_frame = tk.Frame(self.root)
        self.info_frame.config(Aspect.frame_opt())
        self.info_frame.grid(column=1,row=0, sticky=Aspect.def_sticky)
        self.info_frame.grid_columnconfigure(0, minsize=int(self.window_width / 2))
        self.info = Info(self)

    def init_controls(self):
        self.control_frame = tk.Frame(self.root)
        self.control_frame.config(Aspect.frame_opt())
        self.control_frame.grid(column=1,row=1, sticky=Aspect.def_sticky)
        self.control_frame.grid_columnconfigure(0, minsize=int(self.window_width / 2))
        self.controls = Controls(self)

    def simulate(self):
        self.t0 = time.time()
        self.t_1 = - self.dt
        self.t = 0
        self.dt_sim_err = 0
        while self.t < 20:
            time.sleep(self.dt)
            self.t_1 = self.t
            self.t = time.time() - self.t0
            self.dt_sim_err = self.t - self.t_1 - self.dt
            theta = 30.0 * np.sin(self.t)
            self.rocket_view.set_angle(theta)
            Log.print('Simulation error ratio {}:'.format(self.dt_sim_err / self.dt))


class Info:

    def __init__(self, gui):
        self.frame = gui.info_frame
        self.gui = gui
        self.title = tk.Label(self.frame, text='Simulation & Rocket Info')
        self.title.config(Aspect.frame_opt())
        self.title.config(justify=tk.CENTER)
        self.title.grid(row=0, sticky=tk.W + tk.E)
       
        self.play_simu = tk.Button(self.frame, text='Start', command=self.go_and_stop)
        self.play_simu.config(Aspect.button_opt())
        self.play_simu.grid(column=0, row=1, sticky=Aspect.def_sticky)

    def go_and_stop(self):
        if self.gui.go_stop == 'stop':
            self.gui.go_stop = 'start'
            self.play_simu.config(text='Stop')
            self.gui.simulate()
        else:
            self.gui.go_stop == 'stop'
            self.play_simu.config(text='Start')



class Controls:

    def __init__(self, gui):
        self.frame = gui.control_frame
        self.gui = gui
        self.title = tk.Label(self.frame, text='Controls')
        self.title.config(Aspect.frame_opt())
        self.title.config(justify=tk.CENTER)
        self.title.grid(row=0, sticky=tk.W + tk.E)