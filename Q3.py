import math
import random
import numpy as np

X=list()
A=list()
N=np.zeros(4)
count=0

#build table X
while(count<=10000):
    v=random.uniform(0,1)
    u=random.uniform(0,1)
    if(math.sqrt(u**2+v**2)<=1):
        X.append([u,v])
        count+=1

#choose 4 element from table
for i in range(4):
    j=random.randint(0,10000)
    A.append(X[j])

#build vector table
for i in range(4):
    for j in range(4):
        k=np.dot(A[i],A[j])/(np.linalg.norm(A[i])*(np.linalg.norm(A[j])))
        if (k<=0):
            N[i]+=1
