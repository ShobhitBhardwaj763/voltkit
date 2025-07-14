
# voltkit/streamlit_ui/signal_generator_app.py


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from voltkit.core.signals import sine_wave, square_wave, triangular_wave, constant

st.set_page_config(page_title="Signal Generator", layout="centered")

st.title("📡 Signal Generator - VoltKit")

# Sidebar controls
st.sidebar.header("Signal Parameters")
waveform = st.sidebar.selectbox("Waveform Type", ["Sine", "Square", "Triangle", "DC Constant"])
frequency = st.sidebar.slider("Frequency (Hz)", 1, 2000, 100)
amplitude = st.sidebar.slider("Amplitude (V)", 1, 20, 5)
duration = st.sidebar.slider("Duration (s)", 0.01, 2.0, 0.1)
sample_rate = st.sidebar.slider("Sample Rate (Hz)", 500, 20000, 5000)

# Generate signal
if waveform == "Sine":
    t, signal = sine_wave(frequency, amplitude, duration, sample_rate)
elif waveform == "Square":
    t, signal = square_wave(frequency, amplitude, duration, sample_rate)
elif waveform == "Triangle":
    t, signal = triangular_wave(frequency, amplitude, duration, sample_rate)
else:
    t, signal = constant(amplitude, duration, sample_rate)

# Plot signal
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, signal)
ax.set_title(f"{waveform} Wave - {frequency} Hz, {amplitude} V")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (V)")
ax.grid(True)
st.pyplot(fig)

# Export CSV
df = pd.DataFrame({"Time (s)": t, "Amplitude (V)": signal})
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download CSV", data=csv, file_name="signal.csv", mime="text/csv")

# Footer
st.caption("Made with ❤️ using voltkit")
