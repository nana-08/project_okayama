import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2,11)

# ITERATIONS
diagIterThreads = [19,36,52,65,80,95,107,121,134]
diagIterRpi = [19,35.67,39.5,53.6,67.67,79.29,90,103.53,113]
upTriIterThreads = [44,123,1227.6,4789.3,10645.4,47014.3]
upTriIterRpi = []
lowTriIterThreads = []
lowTriIterRpi = []
symIterThreads = []
symIterRpi = []

# TIME
diagTimeThreads = [0.00324,0.01005,0.02378,0.04123,0.06523,0.09537,0.12883,0.16911,0.21951]
diagTimeRpi = [0.53991,2.09453,3.25948,5.09765,7.36286,9.94951,12.85357,15.60778,19.29513]
upTriTimeThreads = [0.00683,0.03656,0.55841,2.95468,8.42703,46.11916] 
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