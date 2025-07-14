import numpy as np
import matplotlib.pyplot as plt


def calculate_rl_phasors(R, L, I, f):
    """
    Computes phasors for V_R, V_L, and V_S in an RL circuit.

    Parameters:
    - R: Resistance (Ohms)
    - L: Inductance (Henries)
    - I: Current (Amps)
    - f: Frequency (Hz)

    Returns:
    - Dictionary with phasors { 'V_R': complex, 'V_L': complex, 'V_S': complex }
    """
    omega = 2 * np.pi * f
    V_R = R * I           # Real
    V_L = omega * L * I   # Imaginary

    V_R_phasor = complex(V_R, 0)
    V_L_phasor = complex(0, V_L)
    V_S = V_R_phasor + V_L_phasor

    return {
        "V_R": V_R_phasor,
        "V_L": V_L_phasor,
        "V_S": V_S
    }


def plot_rl_phasor_diagram(R, L, I, f):
    """
    Plots the phasor diagram for an RL circuit.

    Inputs:
    - R: Resistance (Ohms)
    - L: Inductance (Henries)
    - I: Current (Amps)
    - f: Frequency (Hz)
    """
    phasors = calculate_rl_phasors(R, L, I, f)

    colors = {
        "V_R": "blue",
        "V_L": "red",
        "V_S": "green"
    }

    plt.figure(figsize=(6, 6))
    for label, phasor in phasors.items():
        plt.quiver(
            0, 0,
            phasor.real, phasor.imag,
            angles='xy', scale_units='xy', scale=1,
            color=colors[label], label=label
        )


    plt.grid(True)
    plt.axis('equal')
    plt.xlabel("Real Axis (V)")
    plt.ylabel("Imaginary Axis (V)")
    plt.title("Phasor Diagram for RL Circuit")
    plt.legend()
    plt.tight_layout()
    plt.show()




def calculate_rc_phasors(R, C, I, f):
    """
    Computes phasors for V_R, V_C, and V_S in an RC circuit.

    Parameters:
    - R: Resistance (Ohms)
    - C: Capacitance (Farads)
    - I: Current (Amps)
    - f: Frequency (Hz)

    Returns:
    - Dictionary with phasors { 'V_R': complex, 'V_C': complex, 'V_S': complex }
    """
    omega = 2 * np.pi * f
    V_R = R * I
    V_C = I / (omega * C)

    V_R_phasor = complex(V_R, 0)
    V_C_phasor = complex(0, -V_C)  # Capacitor voltage lags current by 90°
    V_S = V_R_phasor + V_C_phasor

    return {
        "V_R": V_R_phasor,
        "V_C": V_C_phasor,
        "V_S": V_S
    }


def plot_rc_phasor_diagram(R, C, I, f):
    """
    Plots the phasor diagram for an RC circuit.

    Inputs:
    - R: Resistance (Ohms)
    - C: Capacitance (Farads)
    - I: Current (Amps)
    - f: Frequency (Hz)
    """
    phasors = calculate_rc_phasors(R, C, I, f)

    plt.figure(figsize=(6, 6))
    for label, phasor in phasors.items():
        plt.quiver(0, 0, phasor.real, phasor.imag,
                   angles='xy', scale_units='xy', scale=1, label=label)

    plt.grid(True)
    plt.axis('equal')
    plt.xlabel("Real Axis (V)")
    plt.ylabel("Imaginary Axis (V)")
    plt.title("Phasor Diagram for RC Circuit")
    plt.legend()
    plt.tight_layout()
    plt.show()




def calculate_rlc_phasors(R, L, C, I, f):
    """
    Computes phasors for V_R, V_L, V_C, and V_S in an RLC circuit.

    Parameters:
    - R: Resistance (Ohms)
    - L: Inductance (Henries)
    - C: Capacitance (Farads)
    - I: Current (Amps)
    - f: Frequency (Hz)

    Returns:
    - Dictionary with phasors
    """
    omega = 2 * np.pi * f
    V_R = R * I
    V_L = omega * L * I
    V_C = I / (omega * C)

    V_R_phasor = complex(V_R, 0)
    V_L_phasor = complex(0, V_L)
    V_C_phasor = complex(0, -V_C)

    V_total_imag = V_L_phasor.imag + V_C_phasor.imag
    V_S = V_R_phasor + complex(0, V_total_imag)

    return {
        "V_R": V_R_phasor,
        "V_L": V_L_phasor,
        "V_C": V_C_phasor,
        "V_S": V_S
    }


def plot_rlc_phasor_diagram(R, L, C, I, f):
    """
    Plots the phasor diagram for an RLC circuit.

    Inputs:
    - R: Resistance (Ohms)
    - L: Inductance (Henries)
    - C: Capacitance (Farads)
    - I: Current (Amps)
    - f: Frequency (Hz)
    """
    phasors = calculate_rlc_phasors(R, L, C, I, f)

    plt.figure(figsize=(6, 6))
    for label, phasor in phasors.items():
        plt.quiver(0, 0, phasor.real, phasor.imag,
                   angles='xy', scale_units='xy', scale=1, label=label)

    plt.grid(True)
    plt.axis('equal')
    plt.xlabel("Real Axis (V)")
    plt.ylabel("Imaginary Axis (V)")
    plt.title("Phasor Diagram for RLC Circuit")
    plt.legend()
    plt.tight_layout()
    plt.show()

