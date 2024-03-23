import UAV_Class as UAV
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import *

h = 1000 # search area's height
w = 1500 # search area's width
numUAVs = 20
fov = 50
search = UAV.Environment(h,w)
search.initUAVs(numUAVs,fov)
time = 1000

fig1, ax1 = plt.subplots()
ds = []
foundT = None
def animate(step):
    global foundT
    global ani
    if foundT == None:
        if search.targetFound == True:
            foundT = step
    ax1.clear()
    ax1.plot(search.target[0],search.target[1],'r*')
    for uav in search.UAVs:
        ax1.plot(uav.x[0], uav.x[1], 'bd')
    search.updatePos()
    search.updateValue()
    d_i = []
    for uav in search.UAVs:
        d_i.append(uav.d)
    ds.append(d_i)
    search.updateVel()
    ax1.set_xlim(search.xRange[0],search.xRange[1])
    ax1.set_ylim(search.yRange[0],search.yRange[1])
    ax1.set_title('UAV Positions Over Time')
    ax1.set_ylabel('Y')
    ax1.set_xlabel('X')
    ax1.grid(True)

ani = FuncAnimation(fig1, animate, frames=time, interval=1)
ani.save('uav_animation.gif', writer='pillow', fps=50)



fig2, ax2 = plt.subplots()
for i in range(numUAVs):
    ax2.plot([t+1 for t in range(time+1)],[d[i] for d in ds])
ax2.set_title('UAV Distances Over Time')
ax2.set_ylabel('Distance to Target')
ax2.set_xlabel('Time')
ax2.set_xlim(0,foundT+100)
ax2.grid(True)


print(f'The target was found to be at {search.g} at time {foundT}, giving a error of {[np.abs(search.g[0]-search.target[0]),np.abs(search.g[1]-search.target[1])]}')
plt.show()




