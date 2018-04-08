# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:39:04 2018

@author: Chayaphat & Thanapon
"""
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing.dummy import Pool as ThreadPool 
from Initiate import Initiate

    
#input k and Point x1-xn
k = int(input('Input K : '))
n = int(input('Enter the number of Data :'))
x=[]
y=[]
cenpoint=[]
distance=[]
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

centroid = Initiate.InitiateCentroid(k)

Initiate.PointPlot(data)

#find cenpoint
cenpoint = Initiate.FindCenpoint(n,k,data,centroid)
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
while(flag==0):
    if(new == old):
        flag=1
    else:
        cenpoint = Initiate.FindCenpoint(n,k,data,newcen)
        Initiate.PlotCentroid(k,newcen)
        Initiate.PlotData(n,data,cenpoint)
        old = newcen
        newcen = Initiate.CalNewCentroid(n,k,centroid,data,cenpoint)
        new = newcen


