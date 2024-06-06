import matplotlib.pyplot as plt
import numpy as np
import time
import math
from waveform import burst_waveform

mean = 0
std_dev = 15
threshold = 130

max_sig_amp = 120
min_sig_amp = 60

counter = 0
counter_2 = 0

wave_count_1 = 0
wave_count_2 = 0

cond_1 = False
cond_2 = False

t_axis = np.array([0])
signal_1 = np.array([])
signal_2 = np.array([])
events = np.array([])
simulated_sig_1 = np.array([])
simulated_sig_2 = np.array([])


def display_stats(signal_1, signal_2, t_axis, threshold):
    print("plot n°: ", t_axis[-1] // 200)
    print("Last events: ", list(events[-5:]))

    print("Number of events: ", len(events))
    print("--------------------------------------------------------")

    plt.subplot(2, 1, 1)
    plt.plot(t_axis[-200:], signal_1[-200:])
    plt.title("Random signal and random pulses")
    plt.ylabel("Voltage (mV) \n Channel 1")
    plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
    plt.grid(True, lw=0.5)

    plt.subplot(2, 1, 2)
    plt.plot(t_axis[-200:], signal_2[-200:])
    plt.xlabel("Time (ns)")
    plt.ylabel("Voltage (mV) \n Channel 2")
    plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
    plt.grid(True, lw=0.5)

    plt.show()
    plt.clf()
    # file_name="plot "+ str(counter//200)+ ".png"
    # plt.savefig(file_name)


while True:
    time.sleep(0.00001)

    if np.random.randint(201) % 199 == 0:
        wave_count_1 = 0
        amp = np.random.randint(30, 150)
        cond = True

        for i in range(100):
            simulated_sig_1 = np.append(simulated_sig_1, burst_waveform(i, amp))

    if np.random.randint(201) % 199 == 0:
        wave_count_2 = 0
        amp = np.random.randint(30, 150)
        cond = True

        for i in range(100):
            simulated_sig_2 = np.append(simulated_sig_2, burst_waveform(i, amp))

    if cond_1 == False or wave_count_1 == 101:
        simulated_sig_1 = np.append(simulated_sig_1, 0)

    if cond_2 == False or wave_count_1 == 101:
        simulated_sig_2 = np.append(simulated_sig_2, 0)

    rand_point_1 = np.random.normal(loc=mean, scale=std_dev)
    rand_point_2 = np.random.normal(loc=mean, scale=std_dev)

    t_axis = np.append(t_axis, (t_axis[-1] + 1))

    signal_1 = np.append(signal_1, rand_point_1 + simulated_sig_1[wave_count_1])
    signal_2 = np.append(signal_2, rand_point_2 + simulated_sig_2[wave_count_2])


    if signal_1[counter] >= threshold or signal_2[counter] >= threshold:
        a=2




    counter += 1
    wave_count_1 += 1
    wave_count_2 += 1

    if counter % 200 == 0:
        # make list of signal_1s
        display_stats(signal_1, signal_2, t_axis, threshold)
        """ Delete last numbers """
        if len(t_axis) > 1000:
            t_axis = t_axis[200:]
            signal_1 = signal_1[200:]
            simulated_sig_1 = simulated_sig_1[200:]
            counter -= 200
            counter_2 -= 200

        time.sleep(0.5)

