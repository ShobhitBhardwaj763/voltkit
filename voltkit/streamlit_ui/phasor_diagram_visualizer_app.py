
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Phasor Visualizer", layout="centered")
st.title("📐 Phasor Diagram Visualizer (AC Circuits)")

# Sidebar: Component Selection
circuit_type = st.sidebar.selectbox(
    "Choose Circuit Type",
    ["R", "L", "C", "RL", "RC", "RLC"]
)

f = st.sidebar.slider("Frequency (Hz)", 1, 1000, 50)
I = st.sidebar.slider("Current (A)", 0.1, 10.0, 1.0)

R = L = C = 0

if "R" in circuit_type:
    R = st.sidebar.slider("Resistance (Ω)", 1, 1000, 100)

if "L" in circuit_type:
    L = st.sidebar.slider("Inductance (mH)", 1, 1000, 100) * 1e-3

if "C" in circuit_type:
    C = st.sidebar.slider("Capacitance (μF)", 0.1, 1000.0, 10.0) * 1e-6

omega = 2 * np.pi * f

# Compute Phasors
V_R = complex(R * I, 0)
V_L = complex(0, omega * L * I)
V_C = complex(0, -1 / (omega * C) * I) if C != 0 else 0
V_S = V_R + V_L + V_C

phasors = {
    "V_R": V_R if R else 0,
    "V_L": V_L if L else 0,
    "V_C": V_C if C else 0,
    "V_S": V_S
}

colors = {
    "V_R": "blue",
    "V_L": "red",
    "V_C": "orange",
    "V_S": "green"
}

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
for label, phasor in phasors.items():
    if phasor != 0:
        ax.quiver(
            0, 0,
            phasor.real, phasor.imag,
            angles='xy', scale_units='xy', scale=1,
            color=colors[label], label=label
        )

ax.set_title("Phasor Diagram")
ax.set_xlabel("Real Axis (V)")
ax.set_ylabel("Imaginary Axis (V)")
ax.grid(True)
ax.set_aspect('equal')
ax.legend()
st.pyplot(fig)
