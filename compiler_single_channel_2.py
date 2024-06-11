import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform
from functions_2 import *
from trigger_functions_2 import *

#these are values used to generate noise
mean = 0
std_dev = 15

threshold = 100
delay_period= 30 #the delay of time to wait when a threshold is exceeded


t_axis = np.array([0])
signal_0 = np.array([0])
signal_1 = np.array([0])
trigger_times=np.array([0])
print(trigger_times[-1])

likelihood= 8 #probability of occurance of random pulses (Higher makes it less probable, 3 is around 1 occurance per cycle)
plot_size= 200 #Data points in one plot
max_size= 1000 #the maximum number of points in the signal arrays kept at any time (this includes t_axis)

#The classes are used to generate the simulated signals (everything is done 3 times)
amp,  amp_1,  amp_2         = random(np.random.randint(35,150)), random(np.random.randint(35,150)), random(np.random.randint(35,150))
wave_count, wave_count_1, wave_count_2 = markers(0),markers(0),markers(0)
cond,  cond_1,  cond_2      = conditions(False), conditions(False), conditions(False)

amp_1_0,  amp_1_1,  amp_1_2         = random(np.random.randint(35,150)), random(np.random.randint(35,150)), random(np.random.randint(35,150))
wave_count_1_0, wave_count_1_1, wave_count_1_2 = markers(0),markers(0),markers(0)
cond_1_0,  cond_1_1,  cond_1_2      = conditions(False), conditions(False), conditions(False)

#for the trigger system
alarm_0, alarm_1, alarm_m = conditions(False), conditions(False), conditions(False)
delay_0, delay_1, delay_m = markers(0), markers(0), markers(0)

while True:
    t_axis= smart_append(t_axis, t_axis, t_axis[-1]+1, max_size-1) #adds +1 to time each cycle, and limits the len(t_axis) to max_size

    Information_0 =random_generator(mean, std_dev, cond, cond_1, cond_2, wave_count, wave_count_1, wave_count_2,amp, amp_1, amp_2, likelihood)
    signal_0 = smart_append(t_axis, signal_0, Information_0, max_size)

    Information_1 = random_generator(mean, std_dev, cond_1_0, cond_1_1, cond_1_2, wave_count_1_0, wave_count_1_1, wave_count_1_2, amp_1_0 , amp_1_1 , amp_1_2, likelihood)
    signal_1 = smart_append(t_axis, signal_1, Information_1, max_size)

    #display_2_plots(t_axis, signal_0, signal_1, threshold, plot_size)

    #print(len(t_axis),len(signal_1),len( signal_0))
    trigger_times=trigger_v1(t_axis, signal_0, signal_1, max_size, alarm_0, alarm_1,alarm_m ,delay_0, delay_1, delay_m , delay_period, threshold, plot_size, trigger_times)
    save_trigger(t_axis, signal_0, signal_1, trigger_times, plot_size, threshold)
    time.sleep(0.000001)
