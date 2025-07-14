# voltkit/core/bode.py
import matplotlib.pyplot as plt
import numpy as np

def bode_plot(frequencies, H):
    """
    Plot Bode magnitude and phase plots.
    
    Parameters:
        frequencies (array): Frequency range [Hz]
        H: function that returns complex transfer function H(jω)
    """
    omega = 2 * np.pi * np.array(frequencies)
    H_values = np.array([H(w) for w in omega])

    magnitude = 20 * np.log10(np.abs(H_values))
    phase = np.angle(H_values, deg=True)

    plt.figure(figsize=(10, 6))

    # Magnitude plot
    plt.subplot(2, 1, 1)
    plt.semilogx(frequencies, magnitude)
    plt.title('Bode Plot')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True, which='both')

    # Phase plot
    plt.subplot(2, 1, 2)
    plt.semilogx(frequencies, phase)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (degrees)')
    plt.grid(True, which='both')

    plt.tight_layout()
    plt.show()
