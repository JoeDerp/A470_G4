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



testEnv = Environment(40,20)
plt.plot(0,0,'r.')
plt.gca().set_xlim(testEnv.xRange[0], testEnv.xRange[1])
plt.gca().set_ylim(testEnv.yRange[0], testEnv.yRange[1])
plt.gca().grid(True)
plt.show()