import matplotlib.pyplot as plt
import numpy as np
import time

mean = 50
std_dev = 15
threshold= 85

t_axis=np.array([])
signal=np.array([])
events=np.array([])

counter=0

while True:
    time.sleep(0.00001)

    rand_point = np.random.normal(loc=mean, scale=std_dev)
    while rand_point < 10 or rand_point > 100:
        rand_point = np.random.normal(loc=mean, scale=std_dev)


    t_axis = np.append(t_axis, counter)
    signal = np.append(signal, rand_point)
    
    if signal[counter] >= threshold:
        #print("Signal!")
        events=np.append(events , t_axis[counter] )

    counter += 1

    if counter %200==0:
        #make list of signals

        print("plot n°: ", counter//200)
        print("Events: ", counter//200," ", list(events))
        print("Number of events: ", len(events))
        print("--------------------------------------------------------")
        events = np.array([])

        #make plot
        plt.plot(t_axis[-200:], signal[-200:])
        plt.xlabel("Time (ns)")
        plt.ylabel("Voltage (mV)")
        plt.axhline(y=threshold, color='r', lw=1, linestyle='--')
        plt.grid(True, lw=0.5)
        plt.title("random signal")
        plt.show()

        time.sleep(0.5)