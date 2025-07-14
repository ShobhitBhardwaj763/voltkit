# voltkit/core/filters.py

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import streamlit as st

def lowpass_filter(cutoff, fs, order=1):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    return signal.butter(order, normal_cutoff, btype='low', analog=False)

def highpass_filter(cutoff, fs, order=1):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    return signal.butter(order, normal_cutoff, btype='high', analog=False)

def plot_filter_response(b, a, fs, title="Filter Response", show=True, use_streamlit=True):
    w, h = signal.freqz(b, a, worN=8000)
    f = w * fs / (2 * np.pi)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    
    ax1.plot(f, 20 * np.log10(abs(h)))
    ax1.set_title(title)
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Magnitude (dB)')
    ax1.grid(True)

    ax2.plot(f, np.angle(h))
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (radians)')
    ax2.grid(True)

    plt.tight_layout()
    
    if use_streamlit:
        import streamlit as st
        st.pyplot(fig)
    elif show:
        plt.show()