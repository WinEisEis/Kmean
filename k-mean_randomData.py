# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:39:04 2018

@author: Chayaphat & Thanapon
"""
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing.dummy import Pool as ThreadPool 
from Initiate import Initiate
from random import randint
import time
def FindCenpoint(x,y):
    OfCentroid=0
    mins=1000000.0
    for j in range(0,k):
        d=np.sqrt(((x-centroid[j][0])**2)+((y-centroid[j][1])**2))
        if d<=mins:
            mins=d
            OfCentroid=j
    cenpoint=OfCentroid
    return cenpoint

def FindNewCenpoint(x,y):
    OfCentroid=0
    mins=1000000.0
    for j in range(0,k):
        d=np.sqrt(((x-newcen[j][0])**2)+((y-newcen[j][1])**2))
        if d<=mins:
            mins=d
            OfCentroid=j
    cenpoint=OfCentroid
    time.sleep(1)
    return cenpoint


    
#input k and Point x1-xn
k = int(input('Input K : '))
n = int(input('Enter the number of Data :'))
x=[]
y=[]
cenpoint=[]
distance=[]
data=[]
count=0

for i in range (0,n):
    data.append([])
for i in range (0,n):
    for j in range (0,2):
        data[i].append(j)
        data[i][j]=0
for i in range (0,n):
    a = randint(0, 1000)
    b = randint(0, 1000)
    x.append(float(a))
    y.append(float(b))
    
for i in range (0,n):
    for j in range (0,2):
        if j%2==0:
            data[i][j]=x[i]
        else:
            data[i][j]=y[i]

centroid = Initiate.InitiateCentroid(k)

Initiate.PointPlot(data)

#Separate Data to a form of x and y
data = np.array(data)
x,y = data.T
#find cenpoint
pool = ThreadPool()
cenpoint = pool.starmap(FindCenpoint, zip(x,y)) 
pool.close() 
pool.join()
print("Cenpoint :")
print(cenpoint)

#กำหนดสีให้แต่ละกลุ่ม cluster
Initiate.PlotCentroid(k,centroid)
#กำหนดสีให้แต่ละ Data 
Initiate.PlotData(n,data,cenpoint)
#Calculate new centroid
newcen = Initiate.CalNewCentroid(n,k,centroid,data,cenpoint)
print("New centroid :")
print(newcen)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#loop
flag=0
new=newcen
old=centroid
start = time.time()
while(flag==0):
    if(new == old):
        flag=1
    else:
        #cenpoint = Initiate.FindNewCenpoint(n,k,data,newcen)
        count += 1
        print("No: ",count)
        pool = ThreadPool(10)
        cenpoint = pool.starmap(FindNewCenpoint, zip(x,y)) 
        pool.close() 
        pool.join()
        Initiate.PlotCentroid(k,newcen)
        Initiate.PlotData(n,data,cenpoint)
        old = newcen
        newcen = Initiate.CalNewCentroid(n,k,centroid,data,cenpoint)
        new = newcen

end = time.time()

print("Time = ")
print(end-start)
