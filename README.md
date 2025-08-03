
# ⚡ VoltKit — The Open Toolkit for Electrical & Electronics Engineering

![VoltKit Logo](https://voltkit-web.streamlit.app/~/+/media/477830ff6188ca269246b3e68e345ddff24cd145ae266fc35b00f735.jpg)

VoltKit is an open-source Python library designed to make electrical and electronics engineering more practical, visual, and beginner-friendly.

From Ohm's Law to Phasor Diagrams, from FFTs to Streamlit-powered simulations — VoltKit helps students, educators, and makers bring theoretical concepts to life using code.

---

## 🚀 Why VoltKit?

Electrical engineering is filled with complex formulas and repetitive calculations. VoltKit simplifies this by:

- Providing clean and tested Python functions for core EE concepts
- Offering ready-made simulators and calculators
- Including beautiful interactive visualizations using Streamlit
- Helping students build real projects, faster

---

## 🧩 Features (So Far)

| Version | Highlights |
|---------|------------|
| v0.1    | Ohm’s Law, Series & Parallel Resistors, RLC impedance |
| v0.2    | AC Power: Real, Reactive, Apparent, Power Factor |
| v0.3    | Signal generation (sine, square, triangle, DC) |
| v0.4    | Filters (Low-pass, High-pass), Bode Plots |
| v0.5    | FFT Analysis, RC Step Response |
| v1.0    | Phasor Math, RL/RC/RLC Phasor Diagrams, Time-domain Signal
Generator
| v1.0.1  | Real Signal Importing in (csv, wav) formets, Harmonics, Scaling, Signal Stats, Plotting Signal |
 

---

## ⚙️ Installation

```
pip install voltkit
```

Or you can also

Clone the repo and install in development mode:

```bash
git clone https://github.com/ShobhitBhardwaj763/voltkit.git
cd voltkit
pip install -e .
```

## Voltkit v1.0 Collab Notebook with examples

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gL6y9mrg4zuumT950I7BGJqbdwQnsePH)

---

## 🧪 Usage Examples

### Ohm's Law
```python
from voltkit.core import voltage, resistance, current
# voltage(i,r)
# resistance(v,i)
# current(v,r)
v = voltage(2, 5)           # 10 volts
r = resistance(10,2)       # 5 ohms
i = current(10,5)          # 2 amps
```

### RLC Impedance
```python
from voltkit.core import resistor, inductor, capacitor
z_r = resistor(100)                     # 100 Ω
z_l = inductor(10e-3, freq=1000)       # 62.8j Ω
z_c = capacitor(1e-6, freq=1000)       # -159.1j Ω
```

### Phasor Diagram for RL Circuit
```python
from voltkit.core import plot_rl_phasor_diagram
plot_rl_phasor_diagram(R=10, L=0.1, I=1, f=50)
```

### Generate a Sine Wave
```python
from voltkit.core import sine_wave
t, y = sine_wave(freq=50, duration=1, sample_rate=1000, amp=5)
```

## To Plot the sin wave
```python
from voltkit.core import sine_wave
import matplotlib.pyplot as plt
t, y = sine_wave(freq=50, duration=1, sample_rate=1000, amp=5)

plt.figure(figsize=(12, 8))
plt.plot(t, y, label='Sine Wave')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()
plt.show()

```

## Real Signal Processing (v1.0.1)

# Load, analyze and visualize real-world signals easily:
```python
from voltkit.core import (load_csv_signal, add_harmonics, scale_signal, compute_rms, peak_to_peak, signal_energy, compute_thd, plot_signal)

# Load signal from CSV file and plot signal
t,y = load_csv_signal("signal.csv")
plot_signal(t,y, title="Sample Signal")

# Add Harmonics
# Base signal with harmonics
harmonics_dict = {3: 0.5, 5: 0.3}  # Add 3rd and 5th harmonics
t,y = sine_wave(freq=50, amp=5, duration=0.1, fs=5000 )
t,y_harmonic = add_harmonics(t,y, freq, harmonics_dict)
plot_signal(t,y_harmonic, title="Signal with Harmonics")

# Scale the harmonic signal
y_scaled = scale_signal(y_harmonic, factor=2.0)
plot_signal(t, y_scaled, title="Scaled Signal (x2)")

# Analyze the signal
print("RMS", compute_rms(y_scaled))
print("Total Harmonics Distortion": compute_thd(y_scaled))



```
---

## 🖥️ Explore Interactivily

```

Visit our live **VoltKit Simulation Website** built with Streamlit:
👉 [https://voltkit-web.streamlit.app](https://voltkit-web.streamlit.app)

No installation needed, just open in your browser and visualize concepts!

```


### 🧪 Available Simulations on Website

- Signal Generator  
- Bode Plot Explorer  
- FFT Analyzer  
- RC Circuit Visualizer  
- Phasor Diagram Tool  


---
## Example files to understand
- `basic_usage.py`
- `signal_genrator.py`
- `rc_response.py`
- `power_analysis.py`
- `phasor_diagram_example.py`
- `plot_bode_rlc.py`
- `phasor_demo.py`
- `lowpass_filter_demo.py`
- `fft_analysis.py`
- `ac_vs_dc_example.py`
- `signal_analysis_example.py`
- `signal_transform_example.py`
- `signal_stats_example.py`

## To run example files, use this method

```bash
cd voltkit
python examples/example_file_name.py
```

Or just open the rulebook google collab notebook


##  Who Is It For?

-  Students learning EE/ECE fundamentals
-  Teachers building visual classroom demos
-  Makers building small projects and simulations

---

## 🤝 Contributing

Want to contribute or request a feature?

- Submit a PR or open an issue
- Reach me directly at: `voltkit.dev@gmail.com`

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgements

> NumPy - numerical computing
> SciPy - scientific functions
> Pandas - data handling
> Streamlit - interactive web apps
> Matplotlib - plotting

Special thanks to the open-source community.

---

> VoltKit was started with one goal:  
> **To empower electrical engineers to learn and build faster with Python.**  
> If this helped you, feel free to ⭐ star the repo or share it with your peers.
