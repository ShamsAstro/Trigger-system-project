import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform
from functions_1 import *

#these are values used to generate noise
mean = 0
std_dev = 15

threshold = 100

t_axis = np.array([0])
signal = np.array([0])

likelihood= 3 #probability of occurance of random pulses (Higher makes it less probable, 3 is around 1 occurance per cycle)
plot_size= 200 #Data points in one plot

#The classes are used to generate the simulated signals (everything is done 3 times)
amp,  amp_1,  amp_2         = random(np.random.randint(35,150)), random(np.random.randint(35,150)), random(np.random.randint(35,150))
wave_count, wave_count_1, wave_count_2 = markers(0),markers(0),markers(0)
cond,  cond_1,  cond_2      = conditions(False), conditions(False), conditions(False)

while True:
    Information=random_generator(mean, std_dev, cond, cond_1, cond_2, wave_count, wave_count_1, wave_count_2,amp, amp_1, amp_2, likelihood)

    t_axis = np.append(t_axis, (t_axis[-1] + 1))
    signal = np.append(signal,Information)

    display_stats(signal, t_axis, threshold, plot_size)

    #Trigger(information)

    time.sleep(0.00001)
