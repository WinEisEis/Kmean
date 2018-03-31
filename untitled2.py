# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:39:04 2018

@author: Chayaphat & Thanapon
"""
import numpy as np
import matplotlib.pyplot as plt
from Initiate import Initiate

    
#input k and Point x1-xn
k = int(input('Input K : '))
n = int(input('Enter the number of Data :'))
x=[]
y=[]
cenpoint=[]
distance=[]
mins = 0
OfCentroid = 0
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
    x.append(int(a))
    y.append(int(b))

for i in range (0,n):
    for j in range (0,2):
        if j%2==0:
            data[i][j]=x[i]
        else:
            data[i][j]=y[i]

centroid = Initiate.InitiateCentroid(k)

Initiate.PointPlot(data)

for i in range(0,n):
    mins=1000000
    for j in range(0,k):
        d=Initiate.ComPuteEuclideanDistance(data[i][0],data[i][1],centroid[j][0],centroid[j][1])
        if d<=mins:
            mins=d
            OfCentroid=j
    
    cenpoint.append(int(OfCentroid))
print(cenpoint)