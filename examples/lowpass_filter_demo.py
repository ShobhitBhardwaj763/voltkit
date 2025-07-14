

from voltkit.core.filters import lowpass_filter, highpass_filter, plot_filter_response

fs = 1000  # Sampling rate
cutoff = 100  # Cutoff frequency

# Low-pass
b_lp, a_lp = lowpass_filter(cutoff, fs)
plot_filter_response(b_lp, a_lp, fs, title="Low-pass Filter", use_streamlit=False)

# High-pass
b_hp, a_hp = highpass_filter(cutoff, fs)
plot_filter_response(b_hp, a_hp, fs, title="High-pass Filter", use_streamlit=False)

