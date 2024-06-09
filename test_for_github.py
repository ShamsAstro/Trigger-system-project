import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform


class random: #class for generating random numbers used as the amplitude of a signal
    def __init__(self, value):
        self.value=np.random.randint(35,150)
    def random(self):
        self.value=np.random.randint(35,150)

class markers: #this class is for counters used in generating the pulses
    def __init__(self, value):
        self.value=0
    def plus_one(self):
        self.value +=1
    def reset(self):
        self.value =0

class conditions(): #This is used for knowing if a pulse is happening and the code will keep generating the pulse if the value is True
    def __init__(self, state):
        self.state=False
    def set_true(self):
        self.state=True
    def set_false(self):
        self.state=False


def triangle_wave(time,amp):
    slope=5

    triangle_at_t= time *slope
    if triangle_at_t>amp:
        triangle_at_t= 2*amp -time*slope
    elif triangle_at_t<0:
        triangle_at_t=0

    return triangle_at_t

def display_stats(signal, t_axis, threshold, plot_size):
    if len(t_axis)%plot_size==0:

        print("plot n°: ", t_axis[-1] // plot_size)
        print("--------------------------------------------------------")

        plt.plot(t_axis[-plot_size:], signal[-plot_size:])
        plt.xlabel("Time (ns)")
        plt.ylabel("Voltage (mV)")
        plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
        plt.grid(True, lw=0.5)
        plt.title("Random signal and random pulses")
        plt.show()

def random_generator( mean, std_dev, cond, cond_1, cond_2,wave_count,wave_count_1, wave_count_2, amp,amp_1,amp_2, likelihood):

    rand_point = np.random.normal(loc=mean, scale=std_dev) #this generates the background noise
    #rand_point=0

    """These if conditions are repeated 3 times. everytime it checks the "cond_*" condition to choose to generate a pulse"""

    """Pulse number 1 :"""
    if cond.state==False:
        signal = 0
        wave_count.reset()
        #amp=250
        if np.random.randint(likelihood*200)%199==0:
            cond.set_true()

    else:
        #signal=triangle_wave(wave_count, amp)
        signal=burst_waveform(wave_count.value, amp.value)
        wave_count.plus_one()
        if wave_count.value>99:
            cond.set_false()
            amp.random()

    """Pulse number 2 :"""
    if cond_1.state==False:
        signal_1 = 0
        wave_count_1.reset()
        #amp=250
        if np.random.randint(likelihood*200)%199==0:
            cond_1.set_true()

    else:
        #signal=triangle_wave(wave_count, amp)
        signal_1=burst_waveform(wave_count_1.value, amp_1.value)
        wave_count_1.plus_one()
        if wave_count_1.value>99:
            cond_1.set_false()
            amp_1.random()

    """Pulse number 3 :"""
    if cond_2.state == False:
        signal_2 = 0
        wave_count_2.reset()
        # amp=250
        if np.random.randint(likelihood*200)%199 == 0:
            cond_2.set_true()

    else:
        #signal=triangle_wave(wave_count, amp)
        signal_2=burst_waveform(wave_count_2.value, amp_2.value)
        wave_count_2.plus_one()
        if wave_count_2.value>99:
            cond_2.set_false()
            amp_2.random()

    #This adds the noise to the 3 pulses
    next_point = rand_point + signal +signal_1 +signal_2
    return next_point

