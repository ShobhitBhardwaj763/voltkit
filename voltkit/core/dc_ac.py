# voltkit/core/dc_ac.py
import math

AC_TYPES = {'ac', 'alternating', 'sine', 'cosine'}
DC_TYPES = {'dc', 'direct', 'constant'}

def is_ac(signal_type):
    return signal_type.lower() in AC_TYPES

def is_dc(signal_type):
    return signal_type.lower() in DC_TYPES

def rms(peak_voltage):
    return peak_voltage / math.sqrt(2)

def peak(rms_voltage):
    return rms_voltage * math.sqrt(2)
