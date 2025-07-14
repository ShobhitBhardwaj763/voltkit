"""
Ohm's Law Calculations
"""

def voltage(current: float, resistance: float) -> float:
    """Calculate voltage using Ohm's Law: V = I * R"""
    return current * resistance

def current(voltage: float, resistance: float) -> float:
    """Calculate current using Ohm's Law: I = V / R"""
    return voltage / resistance

def resistance(voltage: float, current: float) -> float:
    """Calculate resistance using Ohm's Law: R = V / I"""
    return voltage / current
