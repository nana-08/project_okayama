import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start=2,stop=9)


### PLOT
plt.subplot(121)
regIterThreads = [157,346,2571,20464,54117,76610,16168,614895,77896]
regIterRpi = [126.5,265,1891,15284.2]
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
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="red"))
    
annoRpi = [str(int(y)) for y in regIterRpi]
for xi, yi, text in zip(x, regIterRpi, annoRpi):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(10, -10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="blue"))


plt.subplot(122)
regTimeThread = [0.16432, 0.49525,5.33365,52.23167,162.65825,271.0581,67.46152,2835.89328,394.86779]
regTimeRpi = [3.35060,11.79704,124.23232,1244.56652]
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
                xytext=(10, -10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="red"))
    
annoRpi = [str(round(y, 6))+" s" for y in regTimeRpi]
for xi, yi, text in zip(x, regTimeRpi, annoRpi):
    plt.annotate(text,
                xy=(xi, yi), xycoords='data',
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="blue"))



plt.show()