import matplotlib.pyplot as plt
import numpy as np
import time

mean = 50
std_dev = 15

t_axis=np.array([])
signal=np.array([])


counter=0
print("here!")
while True:
    counter +=1
    time.sleep(0.00001)

    sample = np.random.normal(loc=mean, scale=std_dev)
    while sample < 10 or sample > 100:
        sample = np.random.normal(loc=mean, scale=std_dev)


    t_axis = np.append(t_axis, counter)
    signal = np.append(signal, sample)

    if counter %200==0:
        print("after if", counter)
        plt.plot(t_axis[-200:], signal[-200:])
        plt.xlabel("Time (ns)")
        plt.ylabel("Voltage (mV)")

        plt.grid(True, lw=0.5)
        plt.title("random signal")
        plt.show()
        time.sleep(0.5)