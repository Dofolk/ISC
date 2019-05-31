import math
import random
import numpy as np

count=0
trian_area=0 #set the summation of all triangle area

def calc_area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1,p2,p3
    return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)

#do 100000 times
while (count<100000):
    ptcount=0
    pt=[[],[],[]]
    #1st step:choose 3 point
    while(ptcount<=2):
        v1=2*random.uniform(0,1)-1
        v2=2*random.uniform(0,1)-1
        if(v1**2+v2**2<=1):
            pt[ptcount]=[v1,v2]
            ptcount+=1
    '''#2nd step:choose 3rd point in uniform
    while 1:
        v1=random.uniform(0,1)
        v2=random.uniform(0,1)
        if(v1**2+v2**2<=1):
            u=[v1,v2]
            break'''
    #2nd step:calculate triangle area and sum up all of them
    k=calc_area(pt[0],pt[1],pt[2])
    trian_area+=k
    count+=1

#let p be the probability of triangle
p=4*trian_area/(count*np.pi)

#print out resault
print('凹四邊形機率：')
print(p)
print('凸四邊形機率：')
print(1-p)
