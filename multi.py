# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:39:04 2018

@author: Chayaphat & Thanapon
"""
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import time
from Initiate import Initiate

k = int(input('Input K : '))
n = int(input('Enter the number of Data :'))
global k

def FindCenpoint2(data):
    OfCentroid=0
    mins=1000000.0
    for j in range(0,k):
        d=np.sqrt(((data-1.0)**2)+((data-1.0)**2))
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

def main():  
    #input k and Point x1-xn

 
    x=[]
    y=[]
    centroid=[]
    data=[]
    pool = multiprocessing.Pool(processes=2)
    
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
    
   # centroid = InitiateCentroid(k)

    print(data)
    pool = multiprocessing.Pool()
    start2 = time.time()
    #find cenpoint
    cenpoint2=[]
    data=[1,2,3]
    
    cenpoint2= pool.map(FindCenpoint2,data)
    pool.close()
    pool.join()
    
    print("Cenpoint :")
    print(cenpoint2)
    time.sleep(1)
    end2 = time.time()
    print("Time2 = ",end2-start2)

if __name__ == '__main__':
    main()


