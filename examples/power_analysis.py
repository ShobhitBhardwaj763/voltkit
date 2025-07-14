

import numpy as np
from voltkit.core import instantaneous_power, average_power, reactive_power, apparent_power, power_factor

# Signal setup
t = np.linspace(0, 0.02, 1000)  # Time array from 0 to 0.02s (20ms) with 1000 points
v = 10 * np.sin(2 * np.pi * 50 * t)                    # 10V sine wave at 50Hz
i = 2 * np.sin(2 * np.pi * 50 * t - np.pi / 6)         # 2A sine current lagging by 30°

# Instantaneous power calculation
p = instantaneous_power(v, i)

# RMS values of v and i for AC power calculations
v_rms = 7.07  # (10 / √2)
i_rms = 1.41  # (2 / √2)
phi = np.pi / 6  # 30 degrees in radians

# Power calculations
P_avg = average_power(v_rms, i_rms, phi)
Q = reactive_power(v_rms, i_rms, phi)
S = apparent_power(v_rms, i_rms)
pf = power_factor(phi)

# Output results
print(f"Avg Power: {P_avg:.2f} W")
print(f"Reactive Power: {Q:.2f} VAR")
print(f"Apparent Power: {S:.2f} VA")
print(f"Power Factor: {pf:.2f}")
