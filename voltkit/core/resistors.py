"""
Resistor Calculations: Series and Parallel
"""

def series(*resistors: float) -> float:
    """Calculate total resistance in series configuration"""
    return sum(resistors)

def parallel(*resistors: float) -> float:
    """Calculate total resistance in parallel configuration"""
    if not resistors:
        return 0.0
    return 1 / sum(1 / r for r in resistors)
