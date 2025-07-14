
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from voltkit.core.phasors import phasor_components, time_domain_signal

st.set_page_config(page_title="Phasor Diagram Visualizer", layout="centered")
st.title("📐 Phasor Diagram & Waveform Explorer")

# Sidebar Inputs
st.sidebar.header("🧮 Phasor Parameters")
magnitude = st.sidebar.slider("Magnitude (V or A)", 1.0, 100.0, 10.0)
angle = st.sidebar.slider("Phase Angle (°)", -180, 180, 30)
frequency = st.sidebar.slider("Frequency (Hz)", 10, 100, 50)

# Time domain signal
t = np.linspace(0, 0.05, 1000)
y = time_domain_signal(magnitude, angle, frequency, t)

# Get phasor coordinates
x, y_rect = phasor_components(magnitude, angle)

# Layout
col1, col2 = st.columns(2)

# Plot phasor
with col1:
    fig1, ax1 = plt.subplots()
    ax1.arrow(0, 0, x, y_rect, head_width=2, head_length=3, color='blue')
    ax1.set_xlim(-magnitude - 5, magnitude + 5)
    ax1.set_ylim(-magnitude - 5, magnitude + 5)
    ax1.set_title("Phasor Diagram")
    ax1.set_xlabel("Real Axis")
    ax1.set_ylabel("Imaginary Axis")
    ax1.grid(True)
    ax1.axhline(0, color='gray', lw=0.5)
    ax1.axvline(0, color='gray', lw=0.5)
    st.pyplot(fig1)

# Plot waveform
with col2:
    fig2, ax2 = plt.subplots()
    ax2.plot(t * 1000, y, color='green')
    ax2.set_title("Time-Domain Signal")
    ax2.set_xlabel("Time (ms)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True)
    st.pyplot(fig2)

st.markdown("---")
st.markdown("✅ **Supports single-phase systems for now. Three-phase support coming in VoltKit v1.1!**")
