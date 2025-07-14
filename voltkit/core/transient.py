# voltkit/core/transient.py
import numpy as np

def rc_step_response(R, C, t, V=1):
    """
    RC Charging: Vc(t) = V * (1 - exp(-t/RC))
    """
    tau = R * C
    return V * (1 - np.exp(-t / tau))

def rl_step_response(R, L, t, I=1):
    """
    RL Current Growth: I(t) = I * (1 - exp(-tR/L))
    """
    tau = L / R
    return I * (1 - np.exp(-t / tau))

def rc_discharge(V0, R, C, t):
    """
    RC Discharging: V(t) = V0 * exp(-t/RC)
    """
    tau = R * C
    return V0 * np.exp(-t / tau)

def rl_decay(I0, R, L, t):
    """
    RL Current Decay: I(t) = I0 * exp(-tR/L)
    """
    tau = L / R
    return I0 * np.exp(-t / tau)
