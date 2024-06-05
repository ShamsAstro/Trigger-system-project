import matplotlib.pyplot as plt
import numpy as np
import time

mean = 0
std_dev = 15
threshold = 30

t_axis = np.array([])
signal = np.array([])
events = np.array([])

counter = 0


while True:
    time.sleep(0.00001)

    rand_point = np.random.normal(loc=mean, scale=std_dev)

    t_axis = np.append(t_axis, counter)
    signal = np.append(signal, rand_point)

    if signal[counter] >= threshold:
        # print("Signal!")
        events = np.append(events, t_axis[counter])

    counter += 1



    if len(events)>0:
        print("one")
        plt.plot(t_axis[-200:], signal[-200:])
        plt.xlabel("Time (ns)")
        plt.ylabel("Voltage (mV)")
        plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
        plt.grid(True, lw=0.5)
        plt.title("random signal")
        plt.show()

        #file_name="plot "+ str(counter//200)+ ".png"
        #plt.savefig(file_name)
        events = np.array([])
        time.sleep(0.5)
