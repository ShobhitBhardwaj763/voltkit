
from voltkit.core import ohms_law, resistors, impedance

# Call functions from inside the modules
print("Voltage (2A, 5Ω):", ohms_law.voltage(2, 5))
print("Series Resistance:", resistors.series(1, 2, 3))
print("Parallel Resistance:", resistors.parallel(10, 20, 30))
print("Inductive Impedance:", impedance.inductor(0.1, 50))  # 100mH at 50Hz
