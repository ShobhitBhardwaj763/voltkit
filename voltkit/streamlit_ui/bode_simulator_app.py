
# voltkit/streamlit_ui/bode_simulator_app.py

import streamlit as st
from voltkit.core.filters import lowpass_filter, highpass_filter, plot_filter_response

st.set_page_config(page_title="Bode Plot Simulator", layout="centered")
st.title("🎚️ Bode Plot Simulator - VoltKit")

# Sidebar
filter_type = st.sidebar.selectbox("Filter Type", ["Low-pass", "High-pass"])
cutoff = st.sidebar.slider("Cutoff Frequency (Hz)", 10, 5000, 500)
fs = st.sidebar.slider("Sampling Rate (Hz)", 1000, 20000, 5000)
order = st.sidebar.selectbox("Filter Order", [1, 2, 4, 6])

# Design filter
if filter_type == "Low-pass":
    b, a = lowpass_filter(cutoff, fs, order=order)
else:
    b, a = highpass_filter(cutoff, fs, order=order)

# Plot response
plot_filter_response(b, a, fs, title=f"{filter_type} Filter Bode Plot")
