import matplotlib.pyplot as plt
import numpy as np
import math


def burst_waveform( time, amp ):
    A = amp
    B = 10.0
    C = 10.0
    omega = 1.2
    k = 1.0

    cosine_term   = A * math.cos( omega * time )      # oscillation
    heaviside_term = 1 / (1 + math.exp( -2*k*time ) ) # turn-on (heaviside step function parameterized)
    exponent_term = math.exp( -(time - B)/C )         # attenuation

    voltage = cosine_term * heaviside_term * exponent_term
    return voltage


"""
t_axis = np.array([])
signal = np.array([])

for i in range (100):
    t_axis = np.append(t_axis,i)
    signal = np.append(signal,burst_waveform(i))

plt.plot(t_axis, signal)
plt.xlabel("Time (ns)")
plt.ylabel("Voltage (mV)")
plt.grid(True, lw=0.5)
plt.title("random signal")
plt.show()
"""
