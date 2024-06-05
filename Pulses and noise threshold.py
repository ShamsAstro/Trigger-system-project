import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform

mean = 0
std_dev = 15
threshold = 130

max_sig_amp=120
min_sig_amp=60


counter = 0
wave_count=0
cond= False

t_axis = np.array([0])
signal = np.array([])
events = np.array([])
simulated_sig= np.array([])


def display_stats(events, t_axis, threshold):
    print("plot n°: ", t_axis[-1] // 200)
    print("Last events: ",  list(events[-5:]))

    print("Number of events: ", len(events))
    print("--------------------------------------------------------")

    plt.plot(t_axis[-200:], signal[-200:])
    plt.xlabel("Time (ns)")
    plt.ylabel("Voltage (mV)")
    plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
    plt.grid(True, lw=0.5)
    plt.title("Random signal and random pulses")
    plt.show()
    # file_name="plot "+ str(counter//200)+ ".png"
    # plt.savefig(file_name)

while True:
    time.sleep(0.00001)

    if np.random.randint(201)%199==0:
        wave_count=0
        amp=np.random.randint(30,150)
        cond=True

        for i in range(100):
            simulated_sig=np.append(simulated_sig, burst_waveform(i,amp))


    if cond==False or wave_count==101:
        simulated_sig=np.append(simulated_sig,0)

    rand_point = np.random.normal(loc=mean, scale=std_dev)

    t_axis = np.append(t_axis, (t_axis[-1]+1))
    signal = np.append(signal, rand_point+simulated_sig[wave_count])

    if signal[counter] >= threshold:
        # print("Signal!")
        events = np.append(events, t_axis[counter])


    counter += 1
    wave_count +=1

    if counter % 200 == 0:
        # make list of signals
        display_stats( events, t_axis, threshold)
        """ Delete last numbers """
        if len(t_axis)>1000:

            t_axis = t_axis[200:]
            signal = signal[200:]
            simulated_sig = simulated_sig[200:]
            counter-=200

        time.sleep(0.5)

