import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# LIVE GRAPH UPDATE
fig = plt.figure()
ax = fig.add_subplot(111)
ticks = np.arange(11)

def animate(i):
    pullData = open("points.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    iLine = 0
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            if iLine == 0:
                ax.plot([x],[y], ".r")
            xar.append(float(x))
            yar.append(float(y))
        iLine += 1


    ax.clear()
    ax.set_xlim([-100,100])
    ax.set_ylim([-100,100])
    ax.plot(xar,yar,".b")
    
ani = animation.FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
plt.show()