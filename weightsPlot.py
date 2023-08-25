import matplotlib.pyplot as plt
import numpy as np


# NOT POSSIBLE TO USE YET, STILL WAITING FOR DATA...


fig, (axIter, axTime) = plt.subplots(1,2)

types = ("Equal weights", "Unequal Positive Weights", "Null self-loops", "Unexistant edge between 2 agents", "Chain")



dataIter = {
    'Multithread': (20464, 24104.6, 16726.8, 0, 0),
    'Raspberry Pi': (15284.2, 0, 0, 0, 0),
}

x = np.arange(len(types))  # the label locations
width = 0.33  # the width of the bars
multiplier = 0


for attribute, measurement in dataIter.items():
    offset = width * multiplier
    rects = axIter.bar(x + offset, measurement, width, label=attribute)
    axIter.bar_label(rects)
    multiplier += 1

axIter.set_ylabel('Average time (s)')
axIter.set_title('Performances vs. Weight matrix')
axIter.set_xticks(x + width/2, types)
axIter.legend()



dataTime = {
    'Multithread': (12.82801, 16.07327, 11.24563, 0, 0),
    'Raspberry Pi': (1244.566, 0, 0, 0, 0),
}

x = np.arange(len(types))  # the label locations
width = 0.33  # the width of the bars
multiplier = 0


for attribute, measurement in dataTime.items():
    offset = width * multiplier
    rects = axTime.bar(x + offset, measurement, width, label=attribute)
    axTime.bar_label(rects)
    multiplier += 1

axTime.set_ylabel('Average number of iterations')
axTime.set_title('Performances vs. Weight matrix')
axTime.set_xticks(x + width/2, types)
axTime.legend()


plt.show()