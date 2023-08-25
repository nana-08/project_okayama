import matplotlib.pyplot as plt
import numpy as np


# ITERATIONS
regIterThreads = [157,350,2571,20464,54117,76610,15804,614895,77896]
regIterRpi = [126.5,265,1891,15284.2,43151.83,61298.28,13028.75,313370.44,62296.8]
diagIterThreads = [36,61,85,109,133,159,182,207,228]
diagIterRpi = [36,49,78.5,92.4,115,128.86,160.5,180.44,209.2]
upTriIterThreads = [593,1000,1400,4719,5352581,7229291,7229291,7229291,7229291]
upTriIterRpi = [455,778,1121.25,3673.6,199658.17,884096.43,884096.43,884096.43,884096.43]
lowTriIterThreads = [385,726,1484,4688,3574078,3574078,3574078,3574078,3574078]
lowTriIterRpi = [299,567.33,1178.5,3510.6,589843,589843,589843,589843,589843]
symIterThreads = [205,344,54170,1378,3888,185685,1959263,196547,257104]
symIterRpi = [163.5,269.67,40011.5,1040.4,3037.5,150946.86,150946.86,150946.86,150946.86]

# TIME
regTimeThreads = [0.02408,0.10595,1.18637,12.82801,42.84611,75.85396,18.62617,2835.893,394.867]
regTimeRpi = [3.351,11.797,124.232,1244.566,4541.231,6927.379,1715.195,43484.358,9846.849]
diagTimeThreads = [0.00698,0.02083,0.04488,0.0734,0.10785,0.1518,0.20711,0.28476,0.3682]
diagTimeRpi = [2.42,3.572,6.487,10.514,14.594,17.609,25.942,34.017,45.019]
upTriTimeThreads = [0.08028,0.28124,0.64003,3.03326,10889.80274,63595.1072,63595.1072,63595.1072,63595.1072]
upTriTimeRpi = [13.327,37.56,80.727,342.217,19630.943,94129.2,94129.2,94129.2,94129.2]
lowTriTimeThreads = [0.06029,0.21642,0.68543,2.99773,2819.98782,2819.98782,2819.98782,2819.98782,2819.98782]
lowTriTimeRpi = [9.895,26.209,75.877,300.323,48548.527,48548.527,48548.527,48548.527,48548.527]
symTimeThreads = [0.03296,0.1062,24.79105,0.87391,3.19442,181.87793,2331.1549,275.92817,412.54821]
symTimeRpi = [7.475,14.901,2388.221,93.796,303.122,15827.681,15827.681,15827.681,15827.681]



# PLOT results for each matrix
x = np.arange(2,11)
fig, axs = plt.subplots(2,5,sharex=True)
fig.suptitle("Performances vs number of agents depending on the type of matrix")
fig.supxlabel("Number of agents")

axs[0,0].plot(x, regIterThreads, color='red', label="Multithread")
axs[0,0].plot(x, regIterRpi, color='blue', label="RPi")

axs[0,0].legend()
axs[0,0].set_ylabel("Average number of iterations")
axs[0,0].set_title("B REGULAR")


axs[0,1].plot(x, diagIterThreads, color='red', label="Multithread")
axs[0,1].plot(x, diagIterRpi, color='blue', label="RPi")

axs[0,1].legend()
axs[0,1].set_title("B DIAGONAL")


axs[0,2].plot(x, upTriIterThreads, color='red', label="Multithread")
axs[0,2].plot(x, upTriIterRpi, color='blue', label="RPi")
axs[0,2].scatter([7,7],[7229291,884096.43],c="black",marker="x", label="Last measurement")

axs[0,2].legend()
axs[0,2].set_title("B UPPER TRIANGULAR")


axs[0,3].plot(x, lowTriIterThreads, color='red', label="Multithread")
axs[0,3].plot(x, lowTriIterRpi, color='blue', label="RPi")
axs[0,3].scatter([6,6],[3574078,589843],c="black",marker="x", label="Last measurement")

axs[0,3].legend()
axs[0,3].set_title("B LOWER TRIANGULAR")


axs[0,4].plot(x, symIterThreads, color='red', label="Multithread")
axs[0,4].plot(x, symIterRpi, color='blue', label="RPi")
axs[0,4].scatter([7],[150946.86],c="black",marker="x", label="Last measurement")

axs[0,4].legend()
axs[0,4].set_title("B SYMMETRIC")




axs[1,0].plot(x, regTimeThreads, color='red', label="Multithread")
axs[1,0].plot(x, regTimeRpi, color='blue', label="RPi")

axs[1,0].legend()
axs[1,0].set_ylabel("Time (s)")
axs[1,0].set_title("B REGULAR")


axs[1,1].plot(x, diagTimeThreads, color='red', label="Multithread")
axs[1,1].plot(x, diagTimeRpi, color='blue', label="RPi")

axs[1,1].legend()
axs[1,1].set_title("B DIAGONAL")


axs[1,2].plot(x, upTriTimeThreads, color='red', label="Multithread")
axs[1,2].plot(x, upTriTimeRpi, color='blue', label="RPi")
axs[1,2].scatter([7,7],[63595.1072,94129.2],c="black",marker="x", label="Last measurement")

axs[1,2].legend()
axs[1,2].set_title("B UPPER TRIANGULAR")


axs[1,3].plot(x, lowTriTimeThreads, color='red', label="Multithread")
axs[1,3].plot(x, lowTriTimeRpi, color='blue', label="RPi")
axs[1,3].scatter([6,6],[2819.98782,48548.527],c="black",marker="x", label="Last measurement")

axs[1,3].legend()
axs[1,3].set_title("B LOWER TRIANGULAR")


axs[1,4].plot(x, symTimeThreads, color='red', label="Multithread")
axs[1,4].plot(x, symTimeRpi, color='blue', label="RPi")
axs[1,4].scatter([7],[15827.681],c="black",marker="x", label="Last measurement")

axs[1,4].legend()
axs[1,4].set_title("B SYMMETRIC")



plt.show()



# plot the results for every matrix all together
plt.subplot()



# PLOT RATIO ?
# plt.subplot(121)
# ratioIterReg = [i/j for i,j in zip(regIterThreads, regIterRpi)]
# ratioIterDiag = [i/j for i,j in zip(diagIterThreads, diagIterRpi)]
# ratioIterUpTri = [i/j for i,j in zip(upTriIterThreads, upTriIterRpi)]
# ratioIterLowTri = [i/j for i,j in zip(lowTriIterThreads, lowTriIterRpi)]
# ratioIterSym = [i/j for i,j in zip(symIterThreads, symIterRpi)]
# plt.plot(x, ratioIterReg, label="B regular")
# plt.plot(x, ratioIterDiag, label="B diagonal")
# plt.plot(x, ratioIterUpTri, label="B upper triangular")
# plt.plot(x, ratioIterLowTri, label="B lower triangular")
# plt.plot(x, ratioIterSym, label="B symmetric")
# plt.xlabel("Number of agents")
# plt.ylabel("nbIterationsMultithread/nbIterationsRPi")
# plt.title("Number of iterations ratio multithread to RPi")
# plt.legend()

# plt.subplot(122)
# ratioTimeReg = [i/j for i,j in zip(regTimeThreads, regTimeRpi)]
# ratioTimeDiag = [i/j for i,j in zip(diagTimeThreads, diagTimeRpi)]
# ratioTimeUpTri = [i/j for i,j in zip(upTriTimeThreads, upTriTimeRpi)]
# ratioTimeLowTri = [i/j for i,j in zip(lowTriTimeThreads, lowTriTimeRpi)]
# ratioTimeSym = [i/j for i,j in zip(symTimeThreads, symTimeRpi)]
# plt.plot(x, ratioTimeReg, label="B regular")
# plt.plot(x, ratioTimeDiag, label="B diagonal")
# plt.plot(x, ratioTimeUpTri, label="B upper triangular")
# plt.plot(x, ratioTimeLowTri, label="B lower triangular")
# plt.plot(x, ratioTimeSym, label="B symmetric")
# plt.xlabel("Number of agents")
# plt.ylabel("timeMultithread/timeRpi")
# plt.title("Time ratio multithread to RPi")
# plt.legend()

# plt.show()