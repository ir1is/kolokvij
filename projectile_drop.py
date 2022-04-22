import matplotlib.pyplot as plt
import math
import numpy as np
class ProjectileDrop:
    def __init__(self):
        self.y=[]
        self.vx= []
        self.vy = []
        self.x=[]
        self.y=[]
        self.t = []
        self.a_x =0
        self.h=0
        
    def init(self,h,v0x):
        self.y.append(h)
        self.x.append(0)
        self.t.append(0)
        self.vx.append(v0x)
        self.vy.append(-(v0x/np.cos(np.pi/2))*np.sin(np.pi/2) )
        self.dt = 0.01
        self.g=9.81
        self.a_x =0
        
    def visina(self,h):
        self.h=h
        return self.h

    def akceleracija(self,a,dt=0.01):
        self.a=a
        self.vx = self.vx +self.a*self.dt
        return self.vx

    def fall(self):
        # dy=1
        while self.y[-1]>0:
            self.vy.append(self.vy[-1]-self.g*self.dt)
            self.vx.append(self.vx[-1]+self.a_x*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        print(self.t)
            
        fig,(p1,p2)=plt.subplots(1,2)
        p1.plot(self.x,self.y)
        p1.set_title('x-y')
        p1.set_xlabel('x[m]')
        p1.set_ylabel('h[m]')
        p2.plot(self.t,self.vy)
        p2.set_xlabel('t[s]')
        p2.set_ylabel('Vy[m]')
        p2.set_title('vy-t')
        plt.tight_layout()
        plt.show()
        print(self.y)

    def trajanje(self):
        self.time= np.linspace(0.001,0.1,100)
        for i in len(self.time):
            self.t.append(self.t[-1]+i)
        plt.plot(self.time,self.t)
        plt.set_xlabel('dt')
        plt.set_ylabel('y')
        plt.show()

    def meta(self,x_m,w,vx_v):
        momenat =0
        y_m=0
        while True:
            while (math.dist([x_m,y_m],self.x[-1],self.y[-1]))>w and self.y[-1]>0:
                self.fall()
            if self.y[-1]<0:
                momenat+=self.dt
            else:
                break
        return momenat
        plt.plot(self.)



