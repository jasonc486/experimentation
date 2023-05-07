import numpy as np
import matplotlib.pyplot as plt

#Find the first index where the rocket launches
#Adjust threshold to get desired graph
threshold = 400
minimum = 50

def FirstIndex(arr):
    for i in range(minimum,len(arr)):
        if arr[i] > threshold:
            return i
    return -1

#Find the last index where thrust stops
#Can tell no thrust when the strain gauge reads negative
def LastIndex(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return i
    return -1

fileNames = ["data/15psiWaterT1Raw.txt","data/20psiWaterT2.txt",
             "data/25psiWater.txt",   "data/30psiWaterT1.txt",
             "data/35psiWaterT2.txt",   "data/40psiWaterT2.txt"]
plotNames = ["15 psi",  "20psi",    "25psi",
             "30psi",   "35psi",    "40psi"]
for k in range(0, len(fileNames)):
    #Load the Data File
    #Skip the header of the data file
    print(fileNames[k])
    file_data = np.loadtxt(fileNames[k], dtype=float, skiprows = 20)
    time_interval = 1.0/80.0    #HX711 samples at 80hz
    
    #Cut the data array into only the launch part
    firstPos = FirstIndex(file_data)
    subArray = file_data[firstPos:]
    lastPos = LastIndex(subArray)
    subArray = subArray[:lastPos]
    
    #Convert the gram force into newtons
    subArray = subArray * 9.81 / 1000
    length = len(subArray)
    
    #Plot
    t = np.linspace(0, time_interval * (length), length)
    
    plt.figure()
    plt.title("Thrust of Water Rocket vs. Time: " + plotNames[k])
    plt.xlabel('Time (s)')
    plt.ylabel('Thrust (N)')
    plt.plot(t, subArray)

plt.show()
