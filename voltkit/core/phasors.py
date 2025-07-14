# voltkit/core/phasors.py
import cmath
import math

import numpy as np

def to_rect(mag, angle_deg):
    angle_rad = math.radians(angle_deg)
    return cmath.rect(mag, angle_rad)

def to_polar(c):
    mag, angle_rad = cmath.polar(c)
    return mag, math.degrees(angle_rad)

def phasor_add(p1, p2):
    return p1 + p2

def phasor_mul(p1, p2):
    return p1 * p2

def phasor_div(p1, p2):
    return p1 / p2

def phasor_components(magnitude, angle_deg):
    """
    Converts magnitude and angle to rectangular components.

    Parameters:
    - magnitude: Amplitude of phasor
    - angle_deg: Angle in degrees

    Returns:
    - tuple (x, y): Real and imaginary parts
    """
    angle_rad = np.radians(angle_deg)
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)
    return x, y

def generate_phasors(data):
    """
    Generate phasor components for multiple values.

    Parameters:
    - data: List of tuples [(label, magnitude, angle_deg)]

    Returns:
    - dict: label -> (x, y)
    """
    result = {}
    for label, mag, angle in data:
        result[label] = phasor_components(mag, angle)
    return result

def time_domain_signal(mag, angle_deg, freq, t):
    """
    Generates time-domain sine wave for a phasor.

    Parameters:
    - mag: Peak value
    - angle_deg: Phase shift in degrees
    - freq: Frequency in Hz
    - t: Time array

    Returns:
    - y: signal values
    """
    angle_rad = np.radians(angle_deg)
    return mag * np.sin(2 * np.pi * freq * t + angle_rad)
