# voltkit/core/signal_transform.py

import numpy as np

import numpy as np

def add_harmonics(t: np.ndarray, y: np.ndarray, freq: float, harmonics_dict: dict) -> np.ndarray:
    """
    Adds harmonic components to an existing signal.

    This function adds sine waves at integer multiples of a base frequency to an input signal.
    The time array 't' and the base signal 'y' must be provided.

    Args:
        t (np.ndarray): The time array corresponding to the base signal.
        y (np.ndarray): The base signal to which harmonics will be added.
        freq (float): The fundamental frequency (in Hz) of the harmonics.
        harmonics_dict (dict): A dictionary where keys are the harmonic numbers (e.g., 3 for the 3rd harmonic)
                               and values are their corresponding amplitudes.
                               Example: {3: 0.5, 5: 0.3} adds the 3rd and 5th harmonics.

    Returns:
        np.ndarray: The new signal with added harmonics.
    """
    if t is None or y is None or len(t) == 0 or len(y) == 0:
        print("Error: Input time and signal arrays cannot be empty or None.")
        return y
    
    if len(t) != len(y):
        print("Error: Time array and signal array must have the same length.")
        return y

    # Create a copy of the base signal to avoid modifying the original
    y_with_harmonics = y.copy()

    # Iterate through the dictionary to add each harmonic component
    for k, a in harmonics_dict.items():
        if not isinstance(k, (int, float)) or k <= 0:
            print(f"Warning: Invalid harmonic number '{k}'. Must be a positive number. Skipping.")
            continue
        
        if not isinstance(a, (int, float)):
            print(f"Warning: Invalid amplitude for harmonic '{k}'. Must be a number. Skipping.")
            continue

        # Add the harmonic component to the signal
        y_with_harmonics += a * np.sin(2 * np.pi * freq * k * t)

    return t,y_with_harmonics

def mix_signals(y1: np.ndarray, y2: np.ndarray) -> np.ndarray:
    """
    Mixes two signals by adding them together element-wise.
    Signals must have the same length.

    Args:
        y1 (np.ndarray): The first signal array.
        y2 (np.ndarray): The second signal array.

    Returns:
        np.ndarray: The mixed signal array.
    """
    if y1 is None or y2 is None:
        print("Error: Input signals cannot be None.")
        return np.array([])
        
    if len(y1) != len(y2):
        print("Error: Signals must have the same length to be mixed.")
        # You could also resample one signal to match the other,
        # but this simple function assumes they are already the same length.
        return np.array([])

    return y1 + y2

def scale_signal(signal, factor):
    """
    Scales the amplitude of a signal.

    Args:
        signal (np.ndarray): Input signal
        factor (float): Scale factor

    Returns:
        np.ndarray: Scaled signal
    """
    return signal * factor

def am_modulate(carrier_freq, signal, fs, modulation_index=1.0):
    """
    Applies AM (Amplitude Modulation) to a signal.

    Args:
        carrier_freq (float): Carrier frequency (Hz)
        signal (np.ndarray): Message/baseband signal (normalized)
        fs (int): Sampling rate
        modulation_index (float): Modulation index (0 to 1 typical)

    Returns:
        np.ndarray: AM-modulated signal
    """
    t = np.linspace(0, len(signal) / fs, len(signal))
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    return (1 + modulation_index * signal) * carrier
