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
    
    def PointPlot(data):
        data = np.array(data)
        x,y = data.T
        plt.scatter(x,y,marker = 'o',color = 'blue')
        plt.show()

#คำนวณระยะห่าง
    def ComPuteEuclideanDistance(x,y,kx,ky):
        return np.sqrt(((x-kx)**2)+((y-ky)**2))
    
    def GetColor(k):
        color = []
        Colors = ['red','blue','grey','green','black','pink']
        for i in range(0,k):
            color[i] = Colors[i]
        return color
    
