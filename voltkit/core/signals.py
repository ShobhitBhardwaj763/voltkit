# voltkit/core/signals.py
import numpy as np

def sine_wave(freq, amp, duration, sample_rate=1000, phase=0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return t, amp * np.sin(2 * np.pi * freq * t + np.radians(phase))

def square_wave(freq, amp, duration, sample_rate=1000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return t, amp * np.sign(np.sin(2 * np.pi * freq * t))

def triangular_wave(freq, amp, duration, sample_rate=1000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return t, amp * (2 * np.arcsin(np.sin(2 * np.pi * freq * t)) / np.pi)

def constant(value, duration, sample_rate=1000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return t, np.full_like(t, value)
