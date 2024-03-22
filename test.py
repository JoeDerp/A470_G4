import numpy as np

print(np.random.choice([i+1 for i in range(3)]))

# import numpy as np
# import matplotlib.pyplot as plt

# class UAV:
#     def __init__(self,x,v,w,phi_p,phi_g):
#         self.x = x
#         self.v = v
#         self.w = w
#         self.p = [0,0] # initial best postion of UAV is home position
#         self.phi_p = phi_p
#         self.phi_g = phi_g

# class Environment:
# # Environment represents the scanable area where UAVs will search for target
# # Given height and width, will create a corresponding x and y range centered at the origin
#     def __init__(self,height,width):
#         self.h = height
#         self.w = width
#         self.xRange = [-(width/2),(width/2)]
#         self.yRange = [-(height/2),(height/2)]
#         self.targets = []
#         self.g = [] # best known position of target(s)
#         self.UAVs = []

#     def generateTargets(self, numTargets):
#         for i in range(numTargets):
#             self.targets.append((np.random.uniform(self.xRange[0],self.xRange[1]),np.random.uniform(self.yRange[0],self.yRange[1])))
#             self.g.append((np.random.uniform(self.xRange[0],self.xRange[1]),np.random.uniform(self.yRange[0],self.yRange[1])))
#         return self
    
#     def initUAVs(self, numUAVs):
#         for i in range(numUAVs):
#             angle = ((2*np.pi)/numUAVs)*i
#             v_i = [np.cos(angle),np.sin(angle)]
#             self.UAVs.append(UAV([0,0],v_i,0.8,0.1,0.1))
#             self.UAVs[i].target_i = np.random.choice([t for t in range(len(self.targets))])

#     def updatePos(self):
#         for uav in self.UAVs:
#             for i in uav.x:
#                 uav.x[i] += uav.v[i]
#         return self

#     def updateVel(self,g):
#         for uav in self.UAVs:
#             rP = np.random.uniform(0,1)
#             rG = np.random.uniform(0,1)
#             for i in range(len(uav.v)):
#                 uav.v[i] = uav.w*uav.v[i] + uav.phi_p*rP*(uav.p[i]-uav.x[i]) + uav.phi_g*rG*(self.g[uav.target_i][i]-uav.x[i]) 
#         return self

#     def updateValue(self):
#         if np.sqrt(self.x) < func(self.p):
#             self.p = self.x
#         if func(self.p) < func(g):
#             g = self.p
#         return self.p,g



# testEnv = Environment(100,200)
# testEnv.generateTargets(3)
# testEnv.initUAVs(10)
# plt.plot(0,0,'rp')
# for t in testEnv.targets:
#     plt.plot(t[0],t[1],'b*')
# for u in testEnv.UAVs:
#     plt.gca().arrow(u.x[0], u.x[1], u.v[0], u.v[1], head_width=0.1, head_length=0.1, fc='g', ec='g')
# # plt.gca().set_xlim(testEnv.xRange[0], testEnv.xRange[1])
# # plt.gca().set_ylim(testEnv.yRange[0], testEnv.yRange[1])
# plt.gca().set_xlim(-2, 2)
# plt.gca().set_ylim(-2, 2)
# plt.gca().grid(True)
# plt.show()