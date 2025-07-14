

# voltkit/streamlit_ui/rc_visualizer_app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from voltkit.core.simulator import simulate_rc_dc

st.set_page_config(page_title="RC Response Visualizer", layout="centered")
st.title("⏱️ RC Circuit Step Response")

v_source = st.sidebar.slider("Input Voltage (V)", 1, 20, 5)
r = st.sidebar.slider("Resistance (Ohms)", 100, 10000, 1000)
c = st.sidebar.slider("Capacitance (μF)", 0.1, 1000.0, 1.0)

c_farads = c * 1e-6  # Convert to Farads
t = np.linspace(0, 0.05, 1000)
v = simulate_rc_dc(v_source, r, c_farads, t)

plt.figure(figsize=(10, 4))
plt.plot(t, v)
plt.title("RC Charging Curve")
plt.xlabel("Time (s)")
plt.ylabel("Voltage across Capacitor (V)")
plt.grid(True)
st.pyplot(plt)
