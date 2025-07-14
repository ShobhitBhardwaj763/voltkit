
import numpy as np
from voltkit.core import sine_wave
from voltkit.core.fft import plot_fft

# Generate signal
t, s = sine_wave(100, 5, duration=0.05, sample_rate=5000)  # 100Hz, 5V sine

# Plot its frequency spectrum
plot_fft(s, sample_rate=5000)
