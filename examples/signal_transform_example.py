
import numpy as np
from voltkit.core import (
    add_harmonics,
    mix_signals,
    scale_signal,
    am_modulate,
    plot_signal,
    sine_wave,
    square_wave,
    
)

# Common parameters
fs = 5000            # Sampling rate
duration = 0.02      # 20 ms
freq = 50       # 50 Hz

# 🎵 1. Base signal with harmonics
harmonics_dict = {3: 0.5, 5: 0.3}  # Add 3rd and 5th harmonics
t,y_harmonic = sine_wave(freq=50, amp=5, duration=0.1, fs=5000 )
t,y_harmonic = add_harmonics(t,y_harmonic, freq, harmonics_dict)
plot_signal(t,y_harmonic, title="Signal with Harmonics")

# 🎚️ 2. Scale the harmonic signal
y_scaled = scale_signal(y_harmonic, factor=2.0)
plot_signal(t, y_scaled, title="Scaled Signal (x2)")

# 🎧 3. Mix harmonic signal with a clean sine wave
#clean_sine = np.sin(2 * np.pi * 120 * t)  # 120 Hz sine
t,clean_sine= sine_wave(freq=120, amp=2, duration=0.1, fs=5000)
y_mixed = mix_signals(y_harmonic, clean_sine)
plot_signal(t, y_mixed, title="Mixed Signal: Harmonics + 120Hz")

# 📡 4. AM Modulate the harmonic signal
y_modulated = am_modulate(carrier_freq=1000, signal=y_harmonic, fs=fs, modulation_index=0.5)
plot_signal(t, y_modulated, title="AM Modulated Signal (Carrier: 1kHz)")


# Sine Wave
t,y_square = square_wave(freq=50, amp=5, duration=0.1, fs=5000)

t,y_square = add_harmonics(t,y_square, freq=50, harmonics_dict={3:5})
plot_signal(t,y_square, title="Wave")