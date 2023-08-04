import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2,11)

# ITERATIONS
regIterThreads = [157,346,2571,20464,54117,76610,16168,614895,77896]
regIterRpi = [126.5,265,1891,15284.2,43151.83,61298.28,13028.75,313370.44,62296.8]
diagIterThreads = [36,61,85,109,133,159,182,207,228]
diagIterRpi = []
upTriIterThreads = [593,1000,1400,4719,5352581,7229291]
upTriIterRpi = []
lowTriIterThreads = []
lowTriIterRpi = []
symIterThreads = []
symIterRpi = []

# TIME
regTimeThread = [0.164,0.495,5.333,52.231,162.658,271.058,67.461,2835.893,394.867]
regTimeRpi = [3.351,11.797,124.232,1244.566,4541.231,6927.379,1715.195,43484.358,9846.849]
diagTimeThreads = [0.00698,0.02083,0.04488,0.0734,0.10785,0.1518,0.20711,0.28476,0.3682]
diagTimeRpi = []
upTriTimeThreads = [0.08028,0.28124,0.64003,3.03326,10889.80274,63595.1072] 
upTriTimeRpi = []
lowTriTimeThreads = []
lowTriTimeRpi = []
symTimeThreads = []
symTimeRpi = []


plt.subplot(121)
plt.plot(x, diagIterThreads, "--r", label="MT - B diagonal")
#plt.plot(x, upTriIterThreads, ".r", label="MT - B upper triangular")
plt.plot(x, diagIterRpi, "--b", label="RPi - B diagonal")
plt.xlabel("Number of agents")
plt.ylabel("Number of iterations")
plt.legend()
plt.title("Average number of iterations vs number of agents depending on the type of the B matrix")

plt.subplot(122)
plt.plot(x, diagTimeThreads, "--r", label="MT - B diagonal")
#plt.plot(x, upTriTimeThreads, ".r", label="MT - B upper triangular")
plt.plot(x, diagTimeRpi, "--b", label="RPi - B diagonal")
plt.xlabel("Number of agents")
plt.ylabel("Time (s)")
plt.legend()
plt.title("Average time vs number of agents depending on the type of the B matrix")


plt.show()