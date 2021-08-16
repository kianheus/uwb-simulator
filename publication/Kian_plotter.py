"""
Hello poppet


"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import os

    
DataPathBase = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication\\tdoa40")
for i in range(1):
    print("Plot number:", i)
    DataPath = os.path.join(DataPathBase, "DronePosLog" + str(i) + ".csv")
    PlotDataReader = csv.reader(open(DataPath, "r"))

    Data_Line = next(PlotDataReader)

    Data_Array = np.empty((0, 7))
    for row in PlotDataReader:
        Data_Array = np.append(Data_Array, np.array([[float(i) for i in row]]), axis=0)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
    fig.title = ("Hello")
    ax1.plot(Data_Array[:,1], Data_Array[:,2], label="ekf")
    ax1.plot(Data_Array[:,4], Data_Array[:,5], label="ot")
    ax1.set_title("2D top view")
    ax1.legend()

    ax2.plot(Data_Array[:,0], Data_Array[:,1], label="ekf")
    ax2.plot(Data_Array[:,0], Data_Array[:,4], label="ot")
    ax2.set_title("x-pos vs time")
    #ax2.scatter(Data_Array[:,0], Data_Array[:,1])
    ax2.legend()

    ax3.plot(Data_Array[:,0], Data_Array[:,2], label="ekf")
    ax3.plot(Data_Array[:,0], Data_Array[:,5], label="ot")
    ax3.set_title("y-pos vs time")
    #ax3.scatter(Data_Array[:,0], Data_Array[:,2])
    ax3.legend()

    ax4.plot(Data_Array[:,0], Data_Array[:,3], label="ekf")
    ax4.plot(Data_Array[:,0], Data_Array[:,6], label="ot")
    ax4.set_title("z-pos vs time")
    ax4.legend()

    plt.legend()

savedir = DataPathBase
j = 0
while os.path.isfile(os.path.join(savedir, "fig" + str(j) + ".png")):
    j += 1
    print("hi", j)
print(j)
plt.savefig(os.path.join(savedir, "fig" + str(j)))
plt.show()
