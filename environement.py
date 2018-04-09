import numpy as np
from data import Aspect


class Atm:

    P_0 = 1.013  # hPa
    pressure_decrease_rate = 10000  # meters

    rho_0 = 1.125  # kg.m^-3
    rho_decrease_rate = 10000  # meters

    color_0 = (124, 230, 255)
    color_infinity = (0, 38, 128)

    space_height = 100000  # meters

    @classmethod
    def pressure(cls, z):
        # z in meters with respect to the ground.
        return Atm.P_0 * np.exp(- z / Atm.pressure_decrease_rate)  # APPROXIMATION !

    @classmethod
    def vol_density(cls, z):
        # z in meters with respect to the ground.
        return Atm.rho_0 * np.exp(- z / Atm.rho_decrease_rate) # APPROXIMATION !

    @classmethod
    def air_color(cls, r):
        if r < Earth.radius:
            return Aspect.rgb_to_hex(Atm.color_0)
        elif Earth.radius <= r and r < Atm.space_height + Earth.radius:
            p = (r - Earth.radius) / Atm.space_height
            q = 1 - p
            color = [int(q * Atm.color_0[i] + p * Atm.color_infinity[i]) for i in range(3)]
            return Aspect.rgb_to_hex(tuple(color))
        else:
            return Aspect.rgb_to_hex(Atm.color_infinity) 


class Earth:

    radius = 6371000.0  # meters
    g = 9.81  # on ground


class Physics:

    G = 6.674e-11  # m^3.kg^-1.s^-1