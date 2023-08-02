import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# LIVE GRAPH UPDATE
def animate(i):
        pullData = open("sampleText.txt","r").read()
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        for eachLine in dataArray:
            if len(eachLine)>1:
                x,y = eachLine.split(',')
                xar.append(int(x))
                yar.append(int(y))
        ax.clear()
        ax.plot(xar,yar,".")

def graph():
    ani = animation.FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
    plt.show()


graph()