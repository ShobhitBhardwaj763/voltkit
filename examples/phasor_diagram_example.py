
# Examples

from voltkit.core.phasor_diagram import (
    plot_rl_phasor_diagram,
    plot_rc_phasor_diagram,
    plot_rlc_phasor_diagram
)

# RL
plot_rl_phasor_diagram(R=10, L=0.1, I=1, f=50)

# RC
plot_rc_phasor_diagram(R=10, C=100e-6, I=1, f=50)

# RLC
plot_rlc_phasor_diagram(R=10, L=0.1, C=100e-6, I=1, f=50)

