# examples/ac_vs_dc.py


from voltkit.core import is_ac, is_dc, rms, peak

# Signal checks
print("Signal check:")
print("Is 'AC'? :", is_ac("AC"))
print("Is 'dc'? :", is_dc("dc"))

# Peak ↔ RMS conversions
Vp = 10  # Peak voltage
Vrms = rms(Vp)
print(f"RMS of {Vp}V peak = {Vrms:.2f}V")

Vnew = peak(Vrms)
print(f"Back to peak = {Vnew:.2f}V")
