# voltkit/core/fft.py
import numpy as np
import matplotlib.pyplot as plt

def compute_fft(signal, sample_rate):
    """
    Returns frequency bins and magnitudes using FFT
    """
    N = len(signal)
    freq = np.fft.fftfreq(N, d=1/sample_rate)
    fft_vals = np.fft.fft(signal)
    return freq[:N // 2], np.abs(fft_vals[:N // 2])

def plot_fft(signal, sample_rate):
    """
    Plots FFT of the signal
    """
    freq, mag = compute_fft(signal, sample_rate)
    plt.figure(figsize=(8, 4))
    plt.plot(freq, mag)
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.tight_layout()
    plt.show()
