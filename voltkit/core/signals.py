# voltkit/core/signals.py
import numpy as np
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt

def sine_wave(freq, amp, duration, fs=1000, phase=0):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amp * np.sin(2 * np.pi * freq * t + np.radians(phase))

def square_wave(freq, amp, duration, fs=1000):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amp * np.sign(np.sin(2 * np.pi * freq * t))

def triangular_wave(freq, amp, duration, fs=1000):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, amp * (2 * np.arcsin(np.sin(2 * np.pi * freq * t)) / np.pi)

def constant_wave(value, duration, fs=1000):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return t, np.full_like(t, value)

