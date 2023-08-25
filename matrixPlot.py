import matplotlib.pyplot as plt
import numpy as np


# ITERATIONS
regIterThreads = [157,350,2571,20464,54117,76610,15804,614895,77896]
regIterRpi = [126.5,265,1891,15284.2,43151.83,61298.28,13028.75,313370.44,62296.8]
diagIterThreads = [36,61,85,109,133,159,182,207,228]
diagIterRpi = [36,49,78.5,92.4,115,128.86,160.5,180.44,209.2]
upTriIterThreads = [593,1000,1400,4719,5352581,7229291]
upTriIterRpi = [455,778,1121.25,3673.6,199658.17,884096.43]
lowTriIterThreads = [385,726,1484,4688,3574078]
lowTriIterRpi = [299,567.33,1178.5,3510.6,589843]
symIterThreads = [205,344,54170,1378,3888,185685,1959263,196547,257104]
symIterRpi = [163.5,269.67,40011.5,1040.4,3037.5,150946.86]

# TIME
regTimeThreads = [0.02408,0.10595,1.18637,12.82801,42.84611,75.85396,18.62617,2835.893,394.867]
regTimeRpi = [3.351,11.797,124.232,1244.566,4541.231,6927.379,1715.195,43484.358,9846.849]
diagTimeThreads = [0.00698,0.02083,0.04488,0.0734,0.10785,0.1518,0.20711,0.28476,0.3682]
diagTimeRpi = [2.42,3.572,6.487,10.514,14.594,17.609,25.942,34.017,45.019]
upTriTimeThreads = [0.08028,0.28124,0.64003,3.03326,10889.80274,63595.1072] 
upTriTimeThreadsEnd = [63595.1072,1000000]
upTriTimeRpi = [13.327,37.56,80.727,342.217,19630.943,94129.2]
upTriTimeRpiEnd = [94129.2, 110000]
lowTriTimeThreads = [0.06029,0.21642,0.68543,2.99773,2819.98782]
lowTriTimeRpi = [9.895,26.209,75.877,300.323,48548.527]
symTimeThreads = [0.03296,0.1062,24.79105,0.87391,3.19442,181.87793,2331.1549,275.92817,412.54821]
symTimeRpi = [7.475,14.901,2388.221,93.796,303.122,15827.681]



fig, axs = plt.subplots(2,5,sharex=True)
fig.suptitle("Performances vs number of agents depending on the type of matrix")
fig.supxlabel("Number of agents")

xReguIter = np.arange(2,len(regIterThreads)+2)
axs[0,0].plot(xReguIter, regIterThreads, color='red', label="Multithread")
axs[0,0].plot(xReguIter, regIterRpi, color='blue', label="RPi")

axs[0,0].legend()
axs[0,0].set_ylabel("Average number of iterations")
axs[0,0].set_title("B REGULAR")


xDiagIter = np.arange(2,len(regIterThreads)+2)
axs[0,1].plot(xDiagIter, diagIterThreads, color='red', label="Multithread")
axs[0,1].plot(xDiagIter, diagIterRpi, color='blue', label="RPi")

axs[0,1].legend()
axs[0,1].set_title("B DIAGONAL")


xUpTriIter = np.arange(2,len(upTriIterThreads)+2)
axs[0,2].plot(xUpTriIter, upTriIterThreads, color='red', label="Multithread")
#plt.plot(np.arange(7,len(upTriIterThreadsEnd)+7), upTriIterThreadsEnd, color='hotpink')
axs[0,2].plot(xUpTriIter, upTriIterRpi, color='blue', label="RPi")

axs[0,2].legend()
axs[0,2].set_title("B UPPER TRIANGULAR")


xLowTriIter = np.arange(2,len(lowTriIterThreads)+2)
axs[0,3].plot(xLowTriIter, lowTriIterThreads, color='red', label="Multithread")
axs[0,3].plot(xLowTriIter, lowTriIterRpi, color='blue', label="RPi")

axs[0,3].legend()
axs[0,3].set_title("B LOWER TRIANGULAR")


xSymIter = np.arange(2,len(symIterThreads)+2)
axs[0,4].plot(xSymIter, symIterThreads, color='red', label="Multithread")
axs[0,4].plot(xSymIter, symIterRpi, color='blue', label="RPi")

#axs[4,0].set_xlabel("Number of agents")
axs[0,4].legend()
axs[0,4].set_title("B SYMMETRIC")







xReguTime = np.arange(2,len(regTimeThreads)+2)
axs[1,0].plot(xReguTime, regTimeThreads, color='red', label="Multithread")
axs[1,0].plot(xReguTime, regTimeRpi, color='blue', label="RPi")

axs[1,0].legend()
axs[1,0].set_ylabel("Time (s)")
axs[1,0].set_title("B REGULAR")


xDiagTime = np.arange(2,len(regTimeThreads)+2)
axs[1,1].plot(xDiagTime, diagTimeThreads, color='red', label="Multithread")
axs[1,1].plot(xDiagTime, diagTimeRpi, color='blue', label="RPi")

axs[1,1].legend()
axs[1,1].set_title("B DIAGONAL")


xUpTriTime = np.arange(2,len(upTriTimeThreads)+2)
axs[1,2].plot(xUpTriTime, upTriTimeThreads, color='red', label="Multithread")
#plt.plot(np.arange(7,len(upTriTimeThreadsEnd)+7), upTriTimeThreadsEnd, color='hotpink')
axs[1,2].plot(xUpTriTime, upTriTimeRpi, color='blue', label="RPi")

axs[1,2].legend()
axs[1,2].set_title("B UPPER TRIANGULAR")


xLowTriTime = np.arange(2,len(lowTriTimeThreads)+2)
axs[1,3].plot(xLowTriTime, lowTriTimeThreads, color='red', label="Multithread")
axs[1,3].plot(xLowTriTime, lowTriTimeRpi, color='blue', label="RPi")

axs[1,3].legend()
axs[1,3].set_title("B LOWER TRIANGULAR")


xSymTime = np.arange(2,len(symTimeThreads)+2)
axs[1,4].plot(xSymTime, symTimeThreads, color='red', label="Multithread")
axs[1,4].plot(xSymTime, symTimeRpi, color='blue', label="RPi")

axs[1,4].legend()
axs[1,4].set_title("B SYMMETRIC")





plt.show()