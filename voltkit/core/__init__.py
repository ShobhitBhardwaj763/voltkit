# elektro/core/__init__.py

from .ohms_law import voltage, current, resistance
from .resistors import series, parallel
from .impedance import resistor, inductor, capacitor
from .phasors import to_rect, to_polar, phasor_add, phasor_mul, phasor_div, phasor_components, time_domain_signal, generate_phasors
from .dc_ac import is_ac, is_dc, rms, peak
from .units import scale
from .bode import bode_plot
from .transient import rc_step_response, rl_step_response, rc_discharge, rl_decay
from .signals import sine_wave, square_wave, triangular_wave, constant
# v0.4 additions
from .power import instantaneous_power, average_power, reactive_power, apparent_power, power_factor
from .fft import compute_fft, plot_fft
from .filters import lowpass_filter, highpass_filter, plot_filter_response
# v0.5 additions
from .simulator import simulate_rc_dc
from .phasor_diagram import plot_rl_phasor_diagram, calculate_rl_phasors, calculate_rc_phasors, plot_rc_phasor_diagram, calculate_rlc_phasors, plot_rlc_phasor_diagram


