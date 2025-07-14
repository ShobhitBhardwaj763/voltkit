# voltkit/core/units.py

def scale(value_str):
    value_str = value_str.strip().lower()
    suffixes = {
        'p': 1e-12, 'n': 1e-9, 'u': 1e-6, 'μ': 1e-6,
        'm': 1e-3, 'k': 1e3, 'meg': 1e6, 'g': 1e9
    }

    for suffix, multiplier in suffixes.items():
        if value_str.endswith(suffix):
            try:
                num = float(value_str[:-len(suffix)])
                return num * multiplier
            except ValueError:
                raise ValueError(f"Invalid numeric value in '{value_str}'")
    return float(value_str)
