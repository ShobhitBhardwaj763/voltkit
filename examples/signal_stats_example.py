
import numpy as np
from voltkit.core import (
    sine_wave, compute_rms, signal_energy,
    zero_crossings, dominant_frequency, compute_thd, peak_to_peak, plot_signal
)

# Generate a noisy sine wave
t, signal = sine_wave(freq=50, amp=5, duration=1, fs=1000)
signal += 0.5 * np.random.randn(len(signal))  # Add noise
plot_signal(t, signal, title="Noisy Sine Wave")

print(f"RMS Value: {compute_rms(signal):.2f}")
print(f"Signal Energy: {signal_energy(signal):.2f}")
print(f"Zero Crossings: {zero_crossings(signal)}")
print(f"Dominant Frequency: {dominant_frequency(signal, fs=1000):.2f} Hz")
print(f"Total Harmonic Distortion (THD): {compute_thd(signal, fs=1000):.4f}")
print(f"Peak-to-Peak: {peak_to_peak(signal):.2f} V")
