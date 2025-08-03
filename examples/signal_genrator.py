# examples/signal_generator.py


import matplotlib.pyplot as plt
from voltkit.core import sine_wave, square_wave, triangular_wave, constant

# Common parameters
frequency = 50  # Hz
amplitude = 5   # Volts
duration = 0.1  # seconds
sample_rate = 5000  # samples per second

# Generate waveforms
t1, y1 = sine_wave(frequency, amplitude, duration, sample_rate)
t2, y2 = square_wave(frequency, amplitude, duration, sample_rate)
t3, y3 = triangular_wave(frequency, amplitude, duration, sample_rate)
t4, y4 = constant(3, duration, sample_rate)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t1, y1, label='Sine Wave')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t2, y2, label='Square Wave', color='orange')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t3, y3, label='Triangular Wave', color='green')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t4, y4, label='Constant (3V)', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.suptitle('Generated Signals', fontsize=16, y=1.02)
plt.show()

# Load and Signal Analysis


