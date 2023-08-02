import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2,11)

# ITERATIONS
diagIterThreads = [33,59,84,107,130,156,176,200,222]
diagIterRpi = []
upTriIterThreads = [77,233,2326,9295,24966,70761]
upTriIterRpi = []
lowTriIterThreads = []
lowTriIterRpi = []
symIterThreads = []
symIterRpi = []

# TIME
diagTimeThreads = [0.04289,0.11666,0.16938,0.30011,0.37499,0.52349,0.66855,0.86002,1.10981]
diagTimeRpi = []
upTriTimeThreads = [0.09302,0.33475,4.39994,21.82845,66.59907,227.4724] 
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