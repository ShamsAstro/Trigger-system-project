import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform
#from functions_2 import *

def trigger_v1(t_axis, signal_0, signal_1, max_size, alarm_0, alarm_1,alarm_m,delay_0, delay_1, delay_m ,delay_period, threshold, plot_size, trigger_times):
    signal_0 = signal_0[-max_size:]
    signal_1 = signal_1[-max_size:]

    if alarm_0.state==False and signal_0[-1]>threshold:
        alarm_0.set_true()

    elif alarm_0.state==True:
        delay_0.plus_one()
        if delay_0.value > delay_period:
            alarm_0.set_false()
            delay_0.reset()

    if alarm_1.state == False and signal_1[-1] > threshold:
        alarm_1.set_true()

    elif alarm_1.state == True:
        delay_1.plus_one()
        if delay_1.value > delay_period:
            alarm_1.set_false()
            delay_1.reset()


    if alarm_m.state == True:
        print("here")
        delay_m.plus_one()
        if delay_m.value > delay_period:
            delay_m.reset()
            alarm_m.set_false()
            print("stopped!")

    if alarm_1.state * alarm_0.state and alarm_m.state ==False:
        alarm_m.set_true()
        delay_m.plus_one()



    if alarm_m.state==True and delay_m.value==1:
        #print("Trigger!", delay_m.value)
        trigger_time = t_axis[-1] + (plot_size / 2) #this records the times of triggers, and adds half of the plot_size to record the graph and have th triggered signals in the middle
        return np.append(trigger_times, trigger_time)
    else:
        return trigger_times


def save_trigger(t_axis, signal_0, signal_1, trigger_times, plot_size, threshold):
    last_time=t_axis[-1]

    if last_time==trigger_times[-1] : #and trigger_times[-1]!=0:
        print("TTTT!")
        plt.subplot(2, 1, 1)
        plt.plot(t_axis[-plot_size:], signal_0[-plot_size:])
        plt.title("Random signal and random pulses")
        plt.ylabel("Voltage (mV) \n Channel 1")
        plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
        plt.grid(True, lw=0.5)
        plt.text(1, 1.04, "Trigger \nconfirmed!", transform=plt.gca().transAxes, size=11, ha='right', va='bottom', color="green")

        plt.subplot(2, 1, 2)
        plt.plot(t_axis[-plot_size:], signal_1[-plot_size:])
        plt.xlabel("Time (ns)")
        plt.ylabel("Voltage (mV) \n Channel 2")
        plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
        plt.grid(True, lw=0.5)
        plt.savefig(str(t_axis[-1]))
        plt.show()
    else:
        return None


