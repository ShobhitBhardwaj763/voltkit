# examples/plot_bode_rlc.py


from voltkit.core import bode_plot, impedance
import numpy as np

# RLC series circuit transfer function H(jw) = Vout/Vin across the capacitor
R = 1000  # 1kΩ
L = 10e-3  # 10mH
C = 1e-6   # 1uF

def H(w):
    Z_R = impedance.resistor(R)
    Z_L = impedance.inductor(L, w/(2*np.pi))
    Z_C = impedance.capacitor(C, w/(2*np.pi))
    Z_total = Z_R + Z_L + Z_C
    return Z_C / Z_total

frequencies = np.logspace(1, 6, 500)  # 10 Hz to 1 MHz
bode_plot(frequencies, H)
