import math 
import random
import matplotlib.pyplot as plt
import numpy as np
import time

count=0
X1=list()
X2=list()
X3=list()

def resetfun(x):
    x=0
    return x
    
#part I
    
tStart1=time.time()
while(count<=10000):
    v1=2*random.uniform(0,1)-1
    v2=2*random.uniform(0,1)-1
    v3=2*random.uniform(0,1)-1
    if((v1**2+v2**2+v3**2)<=1):
        X1.append((v1,v2,v3))
        count+=1
    
tEnd1=time.time()
print(tEnd1-tStart1)

#part II

tStart2=time.time()
count=resetfun(count)
while(count<=10000):
    r=random.uniform(0,1)**(1/3)
    theta=random.uniform(0,1)*2*math.pi
    phi=random.uniform(0,1)*math.pi
    x=r*math.sin(phi)*math.cos(theta)
    y=r*math.sin(phi)*math.cos(phi)
    z=r*math.cos(phi)
    X2.append((x,y,z))
    count+=1
    
tEnd2=time.time()
print(tEnd2-tStart2)

#part III

count=resetfun(count)
tStart3=time.time()
while(count<=10000):
    v=random.uniform(0,1)
    u=random.uniform(0,1)
    if(math.sqrt(u**2+v**2)<=1):
        rang=math.sqrt(1-u**2-v**2)
        w=random.uniform(-rang,rang)
        X3.append([u,v,w])
        count+=1
tEnd3=time.time()
print(tEnd3-tStart3)
