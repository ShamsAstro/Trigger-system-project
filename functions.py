import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform



def triangle_wave(time,amp):
    slope=5

    triangle_at_t= time *slope
    if triangle_at_t>amp:
        triangle_at_t= 2*amp -time*slope
    elif triangle_at_t<0:
        triangle_at_t=0

    return triangle_at_t

def display_stats(signal, t_axis):
    if len(t_axis)%200==0:

        print("plot n°: ", t_axis[-1] // 200)
        print("--------------------------------------------------------")

        plt.plot(t_axis[-200:], signal[-200:])
        plt.xlabel("Time (ns)")
        plt.ylabel("Voltage (mV)")
        plt.axhline(y=50, color='r', lw=1, linestyle='--')
        plt.grid(True, lw=0.5)
        plt.title("Random signal and random pulses")
        plt.show()

def random_generator( mean, std_dev, cond, wave_count, amp):
    rand_point = np.random.normal(loc=mean, scale=std_dev)
    #rand_point=0

    if cond==False:
        signal = 0
        wave_count=0
        amp = np.random.randint(35, 150)
        #amp=250
        if np.random.randint(401)%199==0:
            cond=True
    else:
        #signal=triangle_wave(wave_count, amp)
        signal=burst_waveform(wave_count, amp)
        if wave_count>99:
            cond=False
            wave_count=0

    next_point = rand_point + signal

    return next_point, cond, wave_count, amp

