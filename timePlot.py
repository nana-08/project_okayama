import matplotlib.pyplot as plt
import numpy as np

x = [2, 5, 10]

### ITERATIONS
iter2thread = np.array([99, 99]).mean()
iter5thread = np.array([1247, 1247, 1247, 1247, 1247]).mean()
iter10thread = np.array([440636, 440636, 440636, 440636, 440636, 440636, 440636, 440636, 440636, 440636]).mean()

iter2rpi = np.array([111, 98]).mean()
iter5rpi = np.array([1078, 1075, 1073, 1077, 774]).mean()
iter10rpi = np.array([]).mean()

### TIME
time2thread = np.array([0.015, 0.016]).mean()
time5thread = np.array([0.662, 0.663, 0.663, 0.663, 0.661]).mean()
time10thread = np.array([623.673, 623.672, 623.681, 623.677, 623.676, 623.682, 623.672, 623.675, 623.674, 623.679]).mean()

time2rpi = np.array([2.212, 2.15]).mean()
time5rpi = np.array([]).mean()
time10rpi = np.array([]).mean()


### PLOT
plt.subplot(121)
iterThread = [iter2thread, iter5thread, iter10thread]
iterRpi = [iter2rpi, iter5rpi, iter10rpi]
plt.plot(x, iterThread, label="Multithread")
plt.plot(x, iterRpi, label="Raspberry Pi")
plt.xlabel("Number of agents")
plt.ylabel("Number of iterations")

plt.subplot(122)
timeThread = [time2thread, time5thread, time10thread]
timeRpi = [time2rpi, time5rpi, time10rpi]
plt.plot(x, timeThread, label="Multithread")
plt.plot(x, timeRpi, label="Raspberry Pi")
plt.xlabel("Number of agents")
plt.ylabel("Time (seconds)")



plt.show()