import matplotlib.pyplot as plt
import numpy as np
import UAV_Class as UAV

numUAVs = [(i+1) for i in range(25)]
h = 2000 # search area's height
w = 3000 # search area's width
fov = 50
tFound = []
rdSeed = 42
search = UAV.Environment(h,w,rdSeed = rdSeed)
for num in numUAVs:
    search.targetFound = False
    search.UAVs = []
    search.initUAVs(num,fov)
    count = 0
    while True:
        # sim
        search.updatePos()
        search.updateValue()
        if search.targetFound == True:
            tFound.append(count)
            break
        search.updateVel()
        count += 1


coefficients = np.polyfit(numUAVs, tFound, 2)
poly = np.poly1d(coefficients)
yFit = poly(numUAVs)

fig1, ax1 = plt.subplots()
ax1.plot(numUAVs,tFound,label = 'Simulated Runs')
ax1.plot(numUAVs,yFit,'--',label = 'Trendline')
ax1.set_title('Swarm Convergence vs Number of UAVs')
ax1.set_ylabel('Time of Convergence')
ax1.set_xlabel('Number of UAVs')
ax1.grid(True)
ax1.legend()

plt.show()