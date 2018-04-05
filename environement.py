import numpy as np


class Atm:

    P_0 = 1.013  # hPa
    pressure_decrease_rate = 10000  # meters

    rho_0 = 1.125  # kg.m^-3
    rho_decrease_rate = 10000  # meters

    @classmethod
    def pressure(cls, z):
        # z in meters with respect to the ground.
        return Atm.P_0 * np.exp(- z / Atm.pressure_decrease_rate)  # APPROXIMATION !

    @classmethod
    def vol_density(cls, z):
        # z in meters with respect to the ground.
        return Atm.rho_0 * np.exp(- z / Atm.rho_decrease_rate) # APPROXIMATION !