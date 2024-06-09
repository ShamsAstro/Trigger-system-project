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

#The classes used to generate the simulated signals
amp=random(np.random.randint(35,150))
wave_count=markers(0)
cond=conditions(False)

while True:
    Information=random_generator(mean, std_dev, cond, wave_count,amp)

    t_axis = np.append(t_axis, (t_axis[-1] + 1))
    signal = np.append(signal,Information)

    display_stats(signal, t_axis, threshold)

    #Trigger(information)

    time.sleep(0.00001)
