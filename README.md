
# ⚡ VoltKit — The Open Toolkit for Electrical & Electronics Engineering

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
| v1.0    | Phasor Math, RL/RC/RLC Phasor Diagrams, Time-domain Signal Generator |

---

## ⚙️ Installation

Clone the repo and install in development mode:

```bash
git clone https://github.com/ShobhitBhardwaj763/voltkit.git
cd voltkit
pip install -e .
```

---

## 🧪 Usage Examples

### Ohm's Law
```python
from voltkit.core import voltage, resistance, current
v = voltage(i=2, r=5)           # 10 volts
r = resistance(v=10, i=2)       # 5 ohms
i = current(v=10, r=5)          # 2 amps
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
from voltkit.core.phasor_diagram import plot_rl_phasor_diagram
plot_rl_phasor_diagram(R=10, L=0.1, I=1, f=50)
```

### Generate a Sine Wave
```python
from voltkit.core import sine_wave
t, y = sine_wave(freq=50, duration=1, fs=1000)
```

---

## 🖥️ Interactive Streamlit Apps

VoltKit also includes pre-built apps for learning and visualizing concepts. Run them like this:

```bash
streamlit run voltkit/streamlit_ui/signal_generator_app.py
```
(If not work, then open Command Prompt and use this method)
```bash
cd voltkit
streamlit run voltkit/streamlit_ui/signal_generator_app.py
```


### Available Apps:

- `signal_generator_app.py`
- `bode_simulator_app.py`
- `fft_explorer_app.py`
- `rc_visualizer_app.py`
- `phasor_visualizer_app.py`
- `phasor_diagram_visualizer_app.py`


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

## To run example files, use this method

```bash
python examples/example_file_name.py
```

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

---

> VoltKit was started with one goal:  
> **To empower electrical engineers to learn and build faster with Python.**  
> If this helped you, feel free to ⭐ star the repo or share it with your peers.
