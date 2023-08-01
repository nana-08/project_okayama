import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start=2,stop=9)


### PLOT
plt.subplot(121)
iterThread = [237, 541, 11958.4, 8556.3, 6610.1, 11487.9, 243392.6]
iterRpi = [187.5,367.67,8077.25,6492.4,4387.67,8239.857,641279.875]
plt.plot(x, iterThread, "-ro", label="Multithread")
plt.plot(x, iterRpi, "-bo", label="Raspberry Pi")
plt.xlabel("Number of agents")
plt.ylabel("Number of iterations")
plt.legend()
plt.title("Average number of iterations vs number of agents")

annoThread = [str(int(y)) for y in iterThread]
for xi, yi, text in zip(x, iterThread, annoThread):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="red"))
    
annoRpi = [str(int(y)) for y in iterRpi]
for xi, yi, text in zip(x, iterRpi, annoRpi):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(10, -10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="blue"))


plt.subplot(122)
timeThread = [0.03053, 0.15498, 5.38131, 5.27859, 5.1862, 11.3038, 291.905]
timeRpi = [4.56563,17.05344,465.64929,496.56615,386.28109,890.72393,68948.3435]
plt.plot(x, timeThread, "-ro", label="Multithread")
plt.plot(x, timeRpi, "-bo", label="Raspberry Pi")
plt.xlabel("Number of agents")
plt.ylabel("Time (seconds)")
plt.legend()
plt.title("Average time vs number of agents")

annoThread = [str(round(y, 6))+" s" for y in timeThread]
for xi, yi, text in zip(x, timeThread, annoThread):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(10, -10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="red"))
    
annoRpi = [str(round(y, 6))+" s" for y in timeRpi]
for xi, yi, text in zip(x, timeRpi, annoRpi):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="blue"))



plt.show()