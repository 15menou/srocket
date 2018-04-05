import tkinter as tk
from data import *
from rocket import Rocket
from PIL import ImageTk
from PIL import Image

class RocketView:

    def __init__(self, gui):
        self.root = gui.root
        self.gui = gui
        self.rocket = Rocket(gui, self)

        
        self.canvas_width = int(self.gui.window_width / 2)
        self.canvas_height = self.gui.window_height
        self.middle_x = int(self.canvas_width / 2)
        self.middle_y = int(self.canvas_height / 2)

        self.rocket_img = Image.open(Picture.rocket_body)
        self.rocket_pict = ImageTk.PhotoImage(self.rocket_img.rotate(0.0))
        self.canvas = tk.Canvas(self.root)
        self.canvas.config(width=self.canvas_width, height=self.canvas_height)
        self.rocket_picture = self.canvas.create_image(self.middle_x,
                                                       self.middle_y,
                                                       image=self.rocket_pict)
        self.canvas.image = self.rocket_pict
        self.canvas.grid(column=0, row=0,
                         rowspan=100,
                         sticky=Aspect.def_sticky)

    def set_angle(self, angle):
        angle %= 360
        self.canvas.delete(self.rocket_picture)
        self.rocket_pict = ImageTk.PhotoImage(self.rocket_img.rotate(angle))
        self.rocket_picture = self.canvas.create_image(self.middle_x,
                                                       self.middle_y,
                                                       image=self.rocket_pict)
        self.canvas.image = self.rocket_pict
        self.canvas.update()