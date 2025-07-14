# voltkit/core/power.py
import numpy as np

def instantaneous_power(v, i):
    """
    Calculates instantaneous power p(t) = v(t) * i(t)
    """
    return np.multiply(v, i)

import numpy as np

def average_power(v_rms, i_rms, phi):
    """
    Calculates average real power for AC circuits.
    P = Vrms * Irms * cos(phi)

    Parameters:
    - v_rms: Voltage (RMS)
    - i_rms: Current (RMS)
    - phi: Phase angle in radians (between voltage and current)

    Returns:
    - Real power in watts (W)
    """
    return v_rms * i_rms * np.cos(phi)

def reactive_power(v_rms, i_rms, phi):
    """
    Calculates reactive power for AC circuits.
    Q = Vrms * Irms * sin(phi)

    Parameters:
    - v_rms: Voltage (RMS)
    - i_rms: Current (RMS)
    - phi: Phase angle in radians (between voltage and current)

    Returns:
    - Reactive power in VAR
    """
    return v_rms * i_rms * np.sin(phi)

def apparent_power(v_rms, i_rms):
    """
    S = Vrms * Irms
    """
    return v_rms * i_rms

def power_factor(phi):
    """
    PF = cos(phi)
    """
    return np.cos(phi)
