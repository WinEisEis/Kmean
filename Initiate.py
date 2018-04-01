# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:21:49 2018

@author: USER
"""
import numpy as np
import matplotlib.pyplot as plt


class Initiate:
    #วาดจุด centroid ลงกราฟ
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
        plt.title('K-Mean Clustering')
        centroid = np.array(centroid)
        x,y = centroid.T
        plt.scatter(x,y,marker = 'x',color='red')
        return centroids
    
    # กำหนดสี ของ centroid
    def PlotCentroid(k,centroid):
        ColorofCentroid = []
        ColorofCentroids = ['red','blue','grey','green','black','pink']
        centroid = np.array(centroid)
        x,y = centroid.T

        for i in range(0,k):
            #ถ้าไม่ใช้ append มันจะขึ้นว่า index out of range
            ColorofCentroid.append(ColorofCentroids[i])
        plt.scatter(x,y,marker = 'x',color = ColorofCentroid)
        
    # กำหนดสีให้กับ Data
    def PlotData(n,data,cenpoint):
        ColorofData = []
        data = np.array(data)
        x,y = data.T
        for i in range(0,n):
            if cenpoint[i] == 0:
                ColorofData.append('red')
            elif cenpoint[i] == 1:
                ColorofData.append('blue')
            elif cenpoint[i] == 2:
                ColorofData.append('grey')
            elif cenpoint[i] == 3:
                ColorofData.append('green')
            elif cenpoint[i] == 4:
                ColorofData.append('black')
            elif cenpoint[i] == 5:
                ColorofData.append('pink')
            else:
                ColorofData.append('yellow')
        plt.scatter(x,y,marker = 'o',color = ColorofData)
        plt.show()
        
    def PointPlot(data):
        data = np.array(data)
        x,y = data.T
        plt.scatter(x,y,marker = 'o',color = 'blue')
        plt.show()

#คำนวณระยะห่าง
    def ComPuteEuclideanDistance(x,y,kx,ky):
        return np.sqrt(((x-kx)**2)+((y-ky)**2))
    
    def CalNewCentroid(n,k,centroid,data,cenpoint):
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
        return newcen
    
    def FindCenpoint(n,k,data,centroid):
        mins=0
        OfCentroid=0
        cenpoint=[]
        for i in range(0,n):
            mins=1000000.0
            for j in range(0,k):
                d=Initiate.ComPuteEuclideanDistance(data[i][0],data[i][1],centroid[j][0],centroid[j][1])
                if d<=mins:
                    mins=d
                    OfCentroid=j
            # cenpoint คือ array ที่เก็บหมายเลข cluster ของแต่ละ data ไว้
            cenpoint.append(int(OfCentroid))
        return cenpoint