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

for i in range(0,n):
    mins=1000000.0
    for j in range(0,k):
        d=Initiate.ComPuteEuclideanDistance(data[i][0],data[i][1],centroid[j][0],centroid[j][1])
        if d<=mins:
            mins=d
            OfCentroid=j
    # cenpoint คือ array ที่เก็บหมายเลข cluster ของแต่ละ data ไว้
    cenpoint.append(int(OfCentroid))
print("Cenpoint :")
print(cenpoint)

#<<<<<<< HEAD
#=======
#กำหนดสีให้แต่ละกลุ่ม cluster
Initiate.PlotCentroid(k,centroid)
#กำหนดสีให้แต่ละ Data 
Initiate.PlotData(n,data,cenpoint)

#Calculate new centroid point
newcen=[]
count=[]
#Create an array of newcen EX. [[0,0],[0,0]...]
for i in range (0,k):
    newcen.append([])
    count.append(0)
for i in range (0,k):
    for j in range (0,2):
        newcen[i].append(j)
        newcen[i][j]=0

#Summation of each data in each centroid   
for i in range(0,n):
    point = cenpoint[i]
    
    newcen[point][0] = newcen[point][0]+data[i][0]
    newcen[point][1] = newcen[point][1]+data[i][1]
    count[point] = count[point]+1.0

for i in range(0,k):
    if(count[i]!=0):
        newcen[i][0] = newcen[i][0]/count[i]
        newcen[i][1] = newcen[i][1]/count[i]
    else: #This else is for checking the count ถ้า count=0 แสดงว่าไม่มี data อยู่ในช่วงนั้นเลย
          #ให้เก็บค่าเก่าเอาไว้
        newcen[i][0] = centroid[i][0]
        newcen[i][1] = centroid[i][1]
print("New centroid :")
print(newcen)
print("Count :")
print(count)
#>>>>>>> 92b20e87a5abdfc5a8270333cde7b5c67fc8e529
