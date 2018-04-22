from log import Log
from solid_bodies import Body
from environement import Earth
import tkinter as tk
import numpy as np


class Rocket:

    def __init__(self, gui, rocket_gui):
        self.name = 'first'
        self.gui = gui
        self.rocket_gui = rocket_gui
        self.parts = dict()
        self.r = Earth.radius

        """
        States: [r, theta, phi, dot(r), dot(theta), dot(phi)]^T
        such that:
            - r       : meters  : radius from earth center.
            - theta   : radians : angular position with respect to launch pad
            - phi     : radians : attitude with respect to radial unitary vetor
            - dot(r)      : rad / s     : derivative of r
            - dot(theta)  : rad / s     : derivative of theta
            - dot(phi)    : rad / s     : derivative of phi
        """
        self.state_list = ['r', 'theta', 'phi', 'dr', 'dtheta', 'dphi']
        self.states = np.zeros([6, 1])
        self.set_state('r', Earth.radius)

        self.init_msg()

    def init_msg(self):
        Log.debug('Rocket initialized such that:')
        for state in self.state_list:
            Log.debug('\t- {}_0: \t{} {}'.format(state,
                                                 self.get_state(state)[0],
                                                 self.state_unite(state)))

    def state_unite(self, s):
        i = ''
        f = ''
        if 'r' in s:
            i = 'meter'
        else:
            i = 'radian'
        if 'd' in s:
            f = ' / second'
        return i + f


    def set_state(self, s, val):
        # s is either 'r', 'theta', 'phi', 'dr', 'dtheta' or 'dphi'.
        if s == 'r':
            self.states[0] = val
        elif s == 'theta':
            self.states[1] = val
        elif s == 'phi':
            self.states[2] = val
        elif s == 'dr':
            self.states[3] = val
        elif s == 'dtheta':
            self.states[4] = val
        elif s == 'dphi':
            self.states[5] = val
        else:
            Log.print('{} is not a state.')
            Log.print("s is either 'r', 'theta', 'phi', 'dr', 'dtheta' or 'dphi'.")
            raise ValueError('Input is not a state.')

    def get_state(self, s):
        # s is either 'r', 'theta', 'phi', 'dr', 'dtheta' or 'dphi'.
        if s == 'r':
            return self.states[0]
        elif s == 'theta':
            return self.states[1]
        elif s == 'phi':
            return self.states[2]
        elif s == 'dr':
            return self.states[3]
        elif s == 'dtheta':
            return self.states[4]
        elif s == 'dphi':
            return self.states[5]
        else:
            Log.print('{} is not a state.')
            Log.print("s is either 'r', 'theta', 'phi', 'dr', 'dtheta' or 'dphi'.")
            raise ValueError('Input is not a state.')

    def dyn(self):
        """
        'dyn' is actually the function f such that:
        dot(X) = f(X) where X is the vector of the states of the system.
        """
        return self.states

    def mass(self):
        return sum([part.mass() for part in self.parts])



class RocketPart:

    def __init__(self, mass):
        self.mass = mass
        self.gc = np.zeros([6, 1])
        self.category = ''

    def gravity_center(self):
        """
        It has to be expressed in the rocket's frame.
        """
        return self.gc

    def mass(self):
        return self.mass


class Engine(RocketPart):

    def __init__(self, mass):
        RocketPart.__init__(self, mass)
        self.category = 'engine'


class Tank(RocketPart):

    def __init__(self, mass):
        RocketPart.__init__(self, mass)
        self.category = 'tank'