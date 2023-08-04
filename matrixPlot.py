import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2,11)

# ITERATIONS
diagIterThreads = [36,61,85,109,133,159,182,207,228]
diagIterRpi = []
upTriIterThreads = [593,1000,1400,4719,5352581]
upTriIterRpi = []
lowTriIterThreads = []
lowTriIterRpi = []
symIterThreads = []
symIterRpi = []

# TIME
diagTimeThreads = [0.00698,0.02083,0.04488,0.0734,0.10785,0.1518,0.20711,0.28476,0.3682]
diagTimeRpi = []
upTriTimeThreads = [0.08028,0.28124,0.64003,3.03326,10889.80274] 
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