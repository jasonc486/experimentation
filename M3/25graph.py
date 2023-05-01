import numpy as np
import matplotlib.pyplot as plt

file_data = np.loadtxt("data/20psiAirRaw.txt", dtype = float)
time_interval = 1.0/80.0    #HX711 samples at 80hz
subArray = file_data[:266]
subArray = subArray[253:]
subArray = subArray * 9.81 / 1000
length = len(subArray)
t = np.arange(0, time_interval * (length), time_interval)

plt.figure()
plt.title("Thrust of rocket vs. time")
plt.xlabel('Time (s)')
plt.ylabel('Thrust (N)')
plt.plot(t, subArray)
plt.show()
