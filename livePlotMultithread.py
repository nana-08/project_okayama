import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# LIVE GRAPH UPDATE

def animate(i):
    pullData = open("points.txt","r").read()
    dataArray = pullData.split('\n')
    xSolution = []
    ySolution = []
    xAgents = []
    yAgents = []
    line = 0
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            if line == 0:
                xSolution.append(x)
                ySolution.append(y)
            xAgents.append(float(x))
            yAgents.append(float(y))
        line += 1


    plt.cla()
    plt.plot(xSolution,ySolution, ".r", label="Actual solution")
    plt.plot(xAgents,yAgents,".b",label="Solutions of the agents")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    
ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)


plt.show()