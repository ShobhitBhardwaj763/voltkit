
# voltkit/streamlit_ui/fft_explorer_app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from voltkit.core.fft import compute_fft

st.set_page_config(page_title="FFT Explorer", layout="centered")
st.title("🧪 FFT Signal Explorer")

st.sidebar.subheader("Signal Generator")
signal_type = st.sidebar.selectbox("Waveform", ["Sine", "Square"])
freq = st.sidebar.slider("Frequency (Hz)", 10, 1000, 100)
amplitude = st.sidebar.slider("Amplitude (V)", 1, 10, 5)
duration = st.sidebar.slider("Duration (s)", 0.01, 1.0, 0.1)
sample_rate = st.sidebar.slider("Sample Rate", 1000, 10000, 5000)

t = np.linspace(0, duration, int(sample_rate * duration))
if signal_type == "Sine":
    y = amplitude * np.sin(2 * np.pi * freq * t)
else:
    y = amplitude * np.sign(np.sin(2 * np.pi * freq * t))

freqs, mag = compute_fft(y, sample_rate)

plt.figure(figsize=(10, 4))
plt.plot(freqs, mag)
plt.title("FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
st.pyplot(plt)
