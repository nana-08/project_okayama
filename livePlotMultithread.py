import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# LIVE GRAPH UPDATE
m = 3

def animate(i):
    xAgents = []
    yAgents = []
    for i in range(1,m+1):
        f = open("points_"+str(i+1)+".txt","r")
        lines = f.readlines()
        xAgenti = []
        yAgenti = []
        for eachLine in lines:
            if len(eachLine)>1:
                x,y = eachLine.split(',')
                xAgenti.append(float(x))
                yAgenti.append(float(y))
        

    plt.cla()
    for i in range(m):
        plt.plot(xAgents[i],yAgents[i],label="Solutions of agent "+str(i+1))
    
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    
ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)


plt.show()