# voltkit/core/signal_stats.py

import numpy as np
from scipy.fft import fft, fftfreq

def compute_rms(signal):
    """
    Returns the RMS value of a signal.
    """
    return np.sqrt(np.mean(np.square(signal)))

def signal_energy(signal):
    """
    Returns the total energy of a signal.
    """
    return np.sum(np.square(signal))

def zero_crossings(signal):
    """
    Counts the number of zero crossings in the signal.
    """
    return np.count_nonzero(np.diff(np.sign(signal)))

def dominant_frequency(signal, fs):
    """
    Estimates the dominant frequency component in the signal.
    """
    N = len(signal)
    yf = np.abs(fft(signal))
    xf = fftfreq(N, 1/fs)

    # Only take positive frequencies
    idx = np.argmax(yf[:N//2])
    return xf[idx]

def compute_thd(signal, fs):
    """
    Calculates Total Harmonic Distortion (THD) of a signal.
    """
    N = len(signal)
    yf = np.abs(fft(signal))[:N//2]
    freqs = fftfreq(N, 1/fs)[:N//2]

    if len(yf) < 2:
        return 0

    fundamental = np.max(yf)
    harmonics = yf[1:]
    harmonic_power = np.sum(np.square(harmonics))
    return np.sqrt(harmonic_power) / fundamental

def peak_to_peak(signal):
    """
    Returns the peak-to-peak value of a signal.
    """
    return np.max(signal) - np.min(signal)
