import tkinter as tk
from solid_bodies import Body
from environement import Earth


class Rocket:

    def __init__(self, gui, rocket_gui):
        self.name = 'first'
        self.gui = gui
        self.rocket_gui = rocket_gui
        self.body = Body({'m':5000,
                          'J':3000})
        self.r = Earth.radius