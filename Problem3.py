import math
import random
import numpy as np

X=list()
A=list()
count=0
pbcount=0

def anglefn(A,b,a,c):
    ba=(A[b][0]-A[a][0],A[b][1]-A[a][1])
    bc=(A[b][0]-A[c][0],A[b][1]-A[c][1])
    angle = np.arccos(np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc)))
    return np.degrees(angle)

#build table X
while(count<=10000):
    v=random.uniform(0,1)
    u=random.uniform(0,1)
    if(math.sqrt(u**2+v**2)<=1):
        X.append([u,v])
        count+=1


#do 10000 times
for i in range(10000):
    vectorlist=list()
    
    #choose 4 element from table
    for i in range(4):
        j=random.randint(0,10000)
        A.append(X[j])

    #run discri
    for i in range(4):
        count_num=0
        v1=v2=v3=0
        if (i==0):
            v1=anglefn(A,0,1,2)
            v2=anglefn(A,0,1,3)
            v3=anglefn(A,0,2,3)
        elif (i==1):
            v1=anglefn(A,1,0,2)
            v2=anglefn(A,1,0,3)
            v3=anglefn(A,1,2,3)
        elif (i==2):
            v1=anglefn(A,2,0,1)
            v2=anglefn(A,2,0,3)
            v3=anglefn(A,2,1,3)
        elif (i==3):
            v1=anglefn(A,3,0,1)
            v2=anglefn(A,3,0,2)
            v3=anglefn(A,3,1,2)
        if (90<=v1<180):
            count_num+=1
            if (90<=v2<180):
                count_num+=1
                if(90<=v3<180):
                    count_num+=1
        if (count_num ==3):
            pbcount+=1
            break

print(pbcount/10000)

#=np.dot(A[i],A[j])/(np.linalg.norm(A[i])*(np.linalg.norm(A[j])))
#cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
#angle = np.arccos(np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc)))
                
