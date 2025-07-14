"""
RLC Impedance Calculations for AC Circuits
Z_R = R
Z_L = jωL
Z_C = 1 / jωC
"""

import cmath

def resistor(R: float) -> complex:
    """Impedance of a resistor: Z = R"""
    return complex(R, 0)

def inductor(L: float, freq: float) -> complex:
    """Impedance of an inductor: Z = jωL"""
    omega = 2 * cmath.pi * freq
    return complex(0, omega * L)

def capacitor(C: float, freq: float) -> complex:
    """Impedance of a capacitor: Z = 1 / jωC"""
    omega = 2 * cmath.pi * freq
    return complex(0, -1 / (omega * C))
