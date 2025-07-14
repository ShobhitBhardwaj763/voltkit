# examples/rc_response.py

import numpy as np
import matplotlib.pyplot as plt
from voltkit.core import transient

# Parameters
R = 1e3  # 1 kΩ
C = 1e-6  # 1 µF
V0 = 5   # Initial voltage
time = np.linspace(0, 0.01, 500)  # 0 to 10ms

# Get responses
charging = transient.rc_step_response(R, C, time, V=V0)
discharging = transient.rc_discharge(V0, R, C, time)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(time * 1000, charging, label='Charging', color='blue')
plt.plot(time * 1000, discharging, label='Discharging', color='red')
plt.title('RC Circuit Response')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
