# voltkit/core/signal_utils.py

import numpy as np
import pandas as pd
from scipy.io import wavfile
import matplotlib.pyplot as plt # Added for plotting functionality

def load_csv_signal(filepath: str, column: int = 1) -> tuple[np.ndarray, np.ndarray] | tuple[None, None]:
    """
    Loads signal data from a CSV file.

    Args:
        filepath (str): The path to the CSV file.
        column (int, optional): The 0-based index of the column to extract as
                                 the signal data. Defaults to 1 (the second column).

    Returns:
        tuple[np.ndarray, np.ndarray] | tuple[None, None]: A tuple containing:
            - t (np.ndarray): The time array (sample indices).
            - y (np.ndarray): The signal amplitude array.
            Returns (None, None) if an error occurs (e.g., file not found, invalid column).
    """
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{filepath}'")
        return None, None
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file at '{filepath}' is empty.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred while reading CSV '{filepath}': {e}")
        return None, None

    if not isinstance(column, int) or column < 0:
        print(f"Error: 'column' must be a non-negative integer. Got {column}")
        return None, None

    if column >= data.shape[1]:
        print(f"Error: Column index {column} is out of bounds for the CSV file. "
              f"The file only has {data.shape[1]} columns.")
        return None, None

    y = data.iloc[:, column].values
    if len(y) == 0:
        print(f"Warning: Selected column {column} in CSV file '{filepath}' is empty.")
        t = np.array([])
    else:
        t = np.arange(len(y))
    return t, y

def load_wav(filepath: str) -> tuple[np.ndarray, np.ndarray, int] | tuple[None, None, None]:
    """
    Loads audio signal data from a WAV file.

    Args:
        filepath (str): The path to the WAV file.

    Returns:
        tuple[np.ndarray, np.ndarray, int] | tuple[None, None, None]: A tuple containing:
            - t (np.ndarray): The time array in seconds.
            - y (np.ndarray): The audio signal amplitude array.
            - fs (int): The sampling frequency (samples per second).
            Returns (None, None, None) if an error occurs.
    """
    try:
        fs, y = wavfile.read(filepath)
    except FileNotFoundError:
        print(f"Error: WAV file not found at '{filepath}'")
        return None, None, None
    except ValueError as e:
        print(f"Error reading WAV file '{filepath}'. It might be corrupt or not a valid WAV format: {e}")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred while reading WAV '{filepath}': {e}")
        return None, None, None

    if len(y) == 0:
        print(f"Warning: WAV file '{filepath}' contains an empty signal.")
        t = np.array([])
    else:
        t = np.arange(len(y)) / fs
    return t, y, fs

def normalize_signal(y: np.ndarray) -> np.ndarray:
    """
    Normalizes a signal to have a maximum absolute amplitude of 1.
    If the signal is all zeros, it returns the signal as is to avoid division by zero.

    Args:
        y (np.ndarray): The input signal array.

    Returns:
        np.ndarray: The normalized signal array.
    """
    if y is None or len(y) == 0:
        print("Warning: Attempted to normalize an empty or None signal. Returning as is.")
        return y
    
    max_abs_val = np.max(np.abs(y))
    if max_abs_val == 0:
        print("Warning: Signal is all zeros. Normalization skipped to avoid division by zero.")
        return y # Return the signal as is if it's all zeros
    
    return y / max_abs_val

def resample_signal(y: np.ndarray, fs_old: float, fs_new: float) -> np.ndarray:
    """
    Resamples a signal from an old sampling frequency to a new one using linear interpolation.

    Args:
        y (np.ndarray): The input signal array.
        fs_old (float): The original sampling frequency of the signal.
        fs_new (float): The desired new sampling frequency.

    Returns:
        np.ndarray: The resampled signal array.
    """
    if y is None or len(y) == 0:
        print("Warning: Attempted to resample an empty or None signal. Returning as is.")
        return y
    
    if fs_old <= 0 or fs_new <= 0:
        print(f"Error: Sampling frequencies must be positive. Got fs_old={fs_old}, fs_new={fs_new}.")
        return y # Return original signal or raise error

    duration = len(y) / fs_old
    t_old = np.linspace(0, duration, len(y), endpoint=False) # endpoint=False is often better for time series
    
    # Calculate number of new samples to maintain duration while avoiding zero-length for very short signals
    num_new_samples = int(fs_new * duration)
    if num_new_samples == 0 and len(y) > 0: # If duration is very small, ensure at least one sample if original had one
        num_new_samples = 1
    elif num_new_samples == 0: # If original signal was empty, new should be too
        return np.array([])

    t_new = np.linspace(0, duration, num_new_samples, endpoint=False)
    
    # Handle cases where original signal might be too short for interpolation
    if len(t_old) < 2 and len(t_new) > 1:
        print("Warning: Original signal too short for meaningful linear interpolation to multiple new points. Duplicating first value.")
        # If original has 0 or 1 point, interp might fail or be trivial.
        # For a single point, just repeat it for the new length
        return np.full(num_new_samples, y[0]) if len(y) > 0 else np.array([])
    elif len(t_old) == 0: # If original signal was empty
        return np.array([])

    return np.interp(t_new, t_old, y)

def trim_signal(t: np.ndarray, y: np.ndarray, start: float, end: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Trims a signal to a specific time interval.

    Args:
        t (np.ndarray): The time array of the signal.
        y (np.ndarray): The signal amplitude array.
        start (float): The desired start time (inclusive) for trimming.
        end (float): The desired end time (inclusive) for trimming.

    Returns:
        tuple[np.ndarray, np.ndarray]: A tuple containing the trimmed time array
                                        and the trimmed signal amplitude array.
                                        Returns empty arrays if the input is empty or range is invalid.
    """
    if t is None or y is None or len(t) == 0 or len(y) == 0:
        print("Warning: Attempted to trim an empty or None signal. Returning empty arrays.")
        return np.array([]), np.array([])
    
    if start >= end:
        print(f"Warning: Start time ({start}) must be less than end time ({end}). Returning empty arrays.")
        return np.array([]), np.array([])

    mask = (t >= start) & (t <= end)
    
    if not np.any(mask): # Check if the mask is all False (no data in range)
        print(f"Warning: No signal data found within the specified trim range [{start}, {end}]. Returning empty arrays.")
        return np.array([]), np.array([])

    return t[mask], y[mask]

def add_noise(y: np.ndarray, snr_db: float = 30) -> np.ndarray:
    """
    Adds Gaussian (random) noise to a signal at a specified Signal-to-Noise Ratio (SNR).

    Args:
        y (np.ndarray): The input signal array.
        snr_db (float, optional): The desired Signal-to-Noise Ratio in decibels (dB).
                                  Defaults to 30 dB.

    Returns:
        np.ndarray: The signal with added noise.
    """
    if y is None or len(y) == 0:
        print("Warning: Attempted to add noise to an empty or None signal. Returning as is.")
        return y

    signal_power = np.mean(y**2)

    if signal_power == 0:
        print("Warning: Signal has zero power (all zeros). Noise cannot be scaled by SNR. "
              "Returning original signal as adding meaningful noise with a defined SNR is not possible.")
        return y # If signal is all zeros, adding noise based on SNR isn't meaningful here.
    
    snr_linear = 10 ** (snr_db / 10)
    noise_power = signal_power / snr_linear
    
    # Ensure noise power is non-negative, though mathematically it should be
    noise_power = max(0, noise_power) 

    # Generate Gaussian noise with mean 0 and standard deviation sqrt(noise_power)
    noise = np.random.normal(0, np.sqrt(noise_power), len(y))
    
    return y + noise

def plot_signal(t: np.ndarray, y: np.ndarray, title: str = "Signal",
                xlabel: str = "Time", ylabel: str = "Amplitude", color: str = 'blue'):
    """
    Plots a signal in the time domain.

    Parameters:
    - t (np.ndarray): time array (x-axis)
    - y (np.ndarray): signal values (y-axis)
    - title (str): plot title
    - xlabel (str): x-axis label
    - ylabel (str): y-axis label
    - color (str): line color
    """
    if t is None or y is None or len(t) == 0 or len(y) == 0:
        print("Warning: Cannot plot an empty or None signal.")
        return

    if len(t) != len(y):
        print("Error: Time array and signal array must have the same length for plotting.")
        return

    plt.figure(figsize=(10, 4))
    plt.plot(t, y, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()