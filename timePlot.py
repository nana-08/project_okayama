import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start=2,stop=11)


### PLOT
plt.subplot(121)
regIterThreads = [157,350,2571,20464,54117,76610,15804,614895,77896]
regIterRpi = [126.5,265,1891,15284.2,43151.83,61298.28,13028.75,313370.44,62296.8]
plt.plot(x, regIterThreads, "-ro", label="Multithread")
plt.plot(x, regIterRpi, "-bo", label="Raspberry Pi")
plt.xlabel("Number of agents")
plt.ylabel("Number of iterations")
plt.legend()
plt.title("Average number of iterations vs number of agents")

annoThread = [str(int(y)) for y in regIterThreads]
for xi, yi, text in zip(x, regIterThreads, annoThread):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(-10, 15), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="red"))
    
annoRpi = [str(int(y)) for y in regIterRpi]
for xi, yi, text in zip(x, regIterRpi, annoRpi):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(-10, -20), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="blue"))


plt.subplot(122)
regTimeThread = [0.02408,0.10595,1.18637,12.82801,42.84611,75.85396,18.62617,2835.893,394.867]
regTimeRpi = [3.351,11.797,124.232,1244.566,4541.231,6927.379,1715.195,43484.358,9846.849]
plt.plot(x, regTimeThread, "-ro", label="Multithread")
plt.plot(x, regTimeRpi, "-bo", label="Raspberry Pi")
plt.xlabel("Number of agents")
plt.ylabel("Time (seconds)")
plt.legend()
plt.title("Average time vs number of agents")

annoThread = [str(round(y, 6))+" s" for y in regTimeThread]
for xi, yi, text in zip(x, regTimeThread, annoThread):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(-10, -20), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="red"))
    
annoRpi = [str(round(y, 6))+" s" for y in regTimeRpi]
for xi, yi, text in zip(x, regTimeRpi, annoRpi):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(-10, 15), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="blue"))



plt.show()