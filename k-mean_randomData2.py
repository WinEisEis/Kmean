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
from tkinter import *
import tkinter.messagebox as tm

#GUI
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_title = Label(self, text="K-Mean Clustering")
        #self.mlabel = Label(self,text='My Label')
        self.label_k = Label(self, text="Number of Centroid (INT or FLOAT): ")
        self.label_data = Label(self, text="Number of Data (INT): ")

        self.entry_k = Entry(self)
        self.entry_data = Entry(self)
        
        self.label_title.grid(row=0)
        self.label_k.grid(row=1, sticky=E)
        self.label_data.grid(row=2, sticky=E)
        self.entry_k.grid(row=1, column=1)
        self.entry_data.grid(row=2, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="OK", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        global k
        global data
        k = self.entry_k.get()
        data = self.entry_data.get()
        k = int(k)
        data = int(data)
        
        root.destroy()
               
        #if username == "john" and password == "password":
        #if isinstance(username, str):
        #    tm.showinfo("Login info", "Welcome John")
        #    print(username)
        #else:
        #    tm.showerror("Login error", "Incorrect username")


root = Tk()
root.geometry('450x150+500+300')
root.title("K-Mean")
lf = LoginFrame(root)
root.mainloop()
n = data
#print(k,data)

#Main function
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
#k = int(input('Input K : '))
#n = int(input('Enter the number of Data :'))
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
        pool = ThreadPool(n)
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
