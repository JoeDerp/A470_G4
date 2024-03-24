import numpy as np
import matplotlib.pyplot as plt

class UAV:
    def __init__(self,x,v,w,phi_p,phi_g,fov):
        self.x = x
        self.v = v
        self.w = w
        self.p = [0,0] # initial best postion of UAV is home position
        self.phi_p = phi_p
        self.phi_g = phi_g
        self.fov = fov
        self.angle = 0
        self.d = 0

class Environment:
# Environment represents the scanable area where UAVs will search for target
# Given height and width, will create a corresponding x and y range centered at the origin
    def __init__(self,height,width,**kwargs):
        if 'rdSeed' in kwargs:
            np.random.seed(kwargs['rdSeed'])
        self.h = height
        self.w = width
        self.xRange = [-(width/2),(width/2)]
        self.yRange = [-(height/2),(height/2)]
        self.target = [np.random.uniform(self.xRange[0],self.xRange[1]),np.random.uniform(self.yRange[0],self.yRange[1])]
        self.g = [np.random.uniform(self.xRange[0],self.xRange[1]),np.random.uniform(self.yRange[0],self.yRange[1])] 
        self.UAVs = []
        self.targetFound = False
    
    def initUAVs(self, numUAVs,fov):
        for i in range(numUAVs):
            angle = ((2*np.pi)/numUAVs)*i
            v_i = [5*np.cos(angle),5*np.sin(angle)]
            self.UAVs.append(UAV([0,0],v_i,0.8,0.2,0.2,fov))
            self.UAVs[i].angle = angle

    def updatePos(self):
        for uav in self.UAVs:
            for i in range(len(uav.x)):
                uav.x[i] += uav.v[i]
        return self

    def updateVel(self):
        for uav in self.UAVs:
            if not self.targetFound:
                if self.xRange[0] <= uav.x[0] <= self.xRange[1] and self.yRange[0] <= uav.x[1] <= self.yRange[1]:
                    # if target not found and uav within env, proceed along initial path
                    pass
                else:
                    # if target not found and uav outside env, return home and rotate initial path
                    uav.angle = np.random.uniform(0, 2*np.pi)
                    v_i = [5*np.cos(uav.angle),5*np.sin(uav.angle)]
                    self.UAVs[self.UAVs.index(uav)] = UAV([0,0],v_i,0.8,0.2,0.2,uav.fov)
            else:
                # if target found, swarm uavs to target
                rP = np.random.uniform(0,1)
                rG = np.random.uniform(0,1)
                for i in range(len(uav.v)):
                    uav.v[i] = uav.w*uav.v[i] + uav.phi_p*rP*(uav.p[i]-uav.x[i]) + uav.phi_g*rG*(self.g[i]-uav.x[i]) 
        return self

    def updateValue(self):
        for uav in self.UAVs:
            uav.d = dist(uav.x,self.target)
            if self.targetFound == False:
                if uav.d <= uav.fov:
                    self.targetFound = True
                    print('Target Found')
                    uav.p = uav.x
                    self.g = uav.p
            else:
                if dist(uav.x,self.target) < dist(uav.p,self.target):
                    uav.p = uav.x
                if dist(uav.p,self.target) < dist(self.g,self.target):
                    self.g = uav.p
        return self
    
def dist(s,o):
    return np.sqrt((o[0]-s[0])**2+(o[1]-s[1])**2)

# testEnv = Environment(100,200)
# testEnv.initUAVs(10)
# for i in range(100):
#     testEnv.updatePos()
#     testEnv.updateValue
# for i in range(100):
#     testEnv.updatePos()
#     testEnv.updateVel()
#     testEnv.updateValue()
# plt.plot(0,0,'rp')
# plt.plot(testEnv.target[0],testEnv.target[1],'b*')
# for u in testEnv.UAVs:
#     plt.plot(u.x[0],u.x[1],'gd')
#      #plt.gca().arrow(u.x[0], u.x[1], u.v[0], u.v[1], head_width=0.1, head_length=0.1, fc='g', ec='g')
# plt.gca().set_xlim(testEnv.xRange[0], testEnv.xRange[1])
# plt.gca().set_ylim(testEnv.yRange[0], testEnv.yRange[1])
# plt.gca().grid(True)
# print('Target at -->',testEnv.target)
# print('Guess at -->',testEnv.g)
# plt.show()