# examples/phasor_demo.py

from voltkit.core import to_rect, to_polar, phasor_add, phasor_mul, phasor_div

# Convert 10∠30° to rectangular
p1 = to_rect(10, 30)
print(f"Rectangular form of 10∠30°: {p1}")

# Convert rectangular back to polar
mag, angle = to_polar(p1)
print(f"Back to polar: magnitude = {mag:.2f}, angle = {angle:.2f}°")

# Phasor addition
p2 = to_rect(5, 45)
result = phasor_add(p1, p2)
print(f"Phasor addition result: {result}")

# Phasor multiplication
mul = phasor_mul(p1, p2)
print(f"Phasor multiplication: {mul}")

# Phasor division
div = phasor_div(p1, p2)
print(f"Phasor division: {div}")
