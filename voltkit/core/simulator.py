# voltkit/core/simulator.py

import numpy as np

def simulate_rc_dc(v_source, r, c, t):
    """Simulates the voltage across a capacitor in an RC charging circuit."""
    tau = r * c
    return v_source * (1 - np.exp(-t / tau))
