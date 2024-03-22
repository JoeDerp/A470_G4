import UAV_Class as UAV
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

h = 1000 # search area's height
w = 1500 # search area's width
numUAVs = 15
search = UAV.Environment(h,w)
search.initUAVs(numUAVs)
time = w
fov = 2

fig1, ax1 = plt.subplots()
def animate(step):
    ax1.clear()
    ax1.plot(search.target[0],search.target[1],'r*')
    for uav in search.UAVs:
        ax1.plot(uav.x[0], uav.x[1], 'bd')
    if step <= search.xRange[1]:
        search.updatePos()
        search.updateValue()
    else:
        search.updatePos()
        search.updateVel()
        search.updateValue()
    ax1.set_xlim(search.xRange[0],search.xRange[1])
    ax1.set_ylim(search.yRange[0],search.yRange[1])
    ax1.set_title('UAV Positions Over Time')
    ax1.set_ylabel('Y')
    ax1.set_xlabel('X')
    ax1.grid(True)

ani = FuncAnimation(fig1, animate, frames=time, interval=20)
ani.save('uav_animation.gif', writer='pillow', fps=5)

