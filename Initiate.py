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
        for i in range (0,k):
            centroid.append([])
        for i in range (0,k):
            for j in range (0,2):
                centroid[i].append(j)
                centroid[i][j]=0    
        
        plt.title('K-Mean Clustering')
        
        #Fix the centroid coordinate for 6 positions
        centroids = np.array(([1,1],[7,7],[15,3],[4,4],[12,6],[9,3]))
        
        for i in range(0,k):
            for j in range(0,2):
                centroid[i][j]=centroids[i][j]
        centroid = np.array(centroid)
        x,y = centroid.T
        plt.scatter(x,y,marker = 'x',color='red')
        return centroid
    
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
    
    
    
