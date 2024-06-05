import matplotlib.pyplot as plt
import numpy as np

mean = 50
std_dev = 15

time=np.array([])
signal=np.array([])

for i in range(200):
    time = np.append(time,i)


    # Generate a random Gaussian sample
    sample = np.random.normal(loc=mean, scale=std_dev)
    while sample < 10 or sample > 100:
        sample = np.random.normal(loc=mean, scale=std_dev)
    signal=np.append(signal, sample)



plt.plot(time, signal)

plt.xlabel("Time (ns)")
plt.ylabel("Voltage (mV)")

plt.grid(True, lw=0.5)
plt.title("random signal")
plt.show()