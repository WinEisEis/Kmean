# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:39:04 2018

@author: Chayaphat & Thanapon
"""
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing.dummy import Pool as ThreadPool 
import time



def FindCenpoint2(x,y):
    OfCentroid=0
    mins=1000000.0
    for j in range(0,k):
        d=np.sqrt(((x-centroid[j][0])**2)+((y-centroid[j][1])**2))
        if d<=mins:
            mins=d
            OfCentroid=j
    # cenpoint คือ array ที่เก็บหมายเลข cluster ของแต่ละ data ไว้
    cenpoint=OfCentroid
    return cenpoint

def InitiateCentroid(k):
    centroid = []
     #Fix the centroid coordinate for 6 positions
    centroids = np.array(([1,1],[7,7],[15,3],[4,4],[12,6],[9,3]))
    for i in range (0,k):
        centroid.append([])
    for i in range (0,k):
        for j in range (0,2):
            centroid[i].append(j)
            centroid[i][j]=centroids[i][j]   
    
    centroids=centroid
    return centroids
    
    
#input k and Point x1-xn
k = int(input('Input K : '))
n = int(input('Enter the number of Data :'))

x=[]
y=[]
centroid=[]
data=[]

for i in range (0,n):
    data.append([])
for i in range (0,n):
    for j in range (0,2):
        data[i].append(j)
        data[i][j]=0
for i in range (0,n):
    print('x[',i+1,'] and y[',i+1,'] :',end=' ')
    a,b = input().split(' ')
    x.append(float(a))
    y.append(float(b))

for i in range (0,n):
    for j in range (0,2):
        if j%2==0:
            data[i][j]=x[i]
        else:
            data[i][j]=y[i]

centroid = InitiateCentroid(k)
print("centroid :",centroid)

print("data :",data)

start2 = time.time()
#find cenpoint
cenpoint2=[]
data = np.array(data)
x,y = data.T
print("X,Y =",x,y)
pool = ThreadPool()
result = pool.starmap(FindCenpoint2, zip(x,y)) 
pool.close() 
pool.join()
#print("Cenpoint :")
#print(cenpoint2)
print("cenpoint :",result)
time.sleep(1)
end2 = time.time()
print("Time2 = ",end2-start2)




