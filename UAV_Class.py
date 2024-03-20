import numpy as np
import matplotlib.pyplot as plt

class Environment:
# Environment represents the scanable area where UAVs will search for target
# Given height and width, will create a corresponding x and y range centered at the origin
    def __init__(self,height,width):
        self.h = height
        self.w = width
        self.xRange = [-(width/2),(width/2)]
        self.yRange = [-(height/2),(height/2)]
        self.targets = []

    def generateTarget(self, numTargets):
        for i in range(numTargets):
            self.targets.append((np.random.uniform(self.xRange[0],self.xRange[1]),np.random.uniform(self.yRange[0],self.yRange[1])))
        return self
    
    def initUAVs(self, numUAVs):
        pass



testEnv = Environment(100,200)
testEnv.generateTarget(3)
print(testEnv.targets)
plt.plot(0,0,'r.')
for t in testEnv.targets:
    plt.plot(t[0],t[1],'b*')
plt.gca().set_xlim(testEnv.xRange[0], testEnv.xRange[1])
plt.gca().set_ylim(testEnv.yRange[0], testEnv.yRange[1])
plt.gca().grid(True)
plt.show()