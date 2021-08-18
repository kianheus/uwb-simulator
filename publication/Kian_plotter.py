"""
Hello poppet


"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import os

Na = 8
N_helpers = 8
RunNr = 3

plot_main = True
plot_helpers = True

big_folder_name = "anchors_" + str(Na) + "_helpers_" + str(N_helpers) + "_run_" + str(RunNr)
print(big_folder_name)
#input_file = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication", big_folder_name)
input_file = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication")

def DataPlotter(DataPath, ax1, ax2, ax3, ax4, fig):
    PlotDataReader = csv.reader(open(DataPath))
    Data_Line = next(PlotDataReader)
    Data_Array = np.ndarray((len(open(DataPath).readlines()) - 1, 7))

    for index, row in enumerate(PlotDataReader):
        Data_Array[index] = np.array([[float(i) for i in row]])

    ax1.plot(Data_Array[:, 1], Data_Array[:, 2], label="ekf")
    ax1.plot(Data_Array[:, 4], Data_Array[:, 5], label="ot")
    ax1.set_title("2D top view")
    ax1.legend()


    ax2.plot(Data_Array[:, 0], Data_Array[:, 1], label="ekf")
    ax2.plot(Data_Array[:, 0], Data_Array[:, 4], label="ot")
    ax2.set_title("x-pos vs time")
    # ax2.scatter(Data_Array[:,0], Data_Array[:,1])
    ax2.legend()

    ax3.plot(Data_Array[:, 0], Data_Array[:, 2], label="ekf")
    ax3.plot(Data_Array[:, 0], Data_Array[:, 5], label="ot")
    ax3.set_title("y-pos vs time")
    # ax3.scatter(Data_Array[:,0], Data_Array[:,2])
    ax3.legend()

    ax4.plot(Data_Array[:, 0], Data_Array[:, 3], label="ekf")
    ax4.plot(Data_Array[:, 0], Data_Array[:, 6], label="ot")
    ax4.set_title("z-pos vs time")
    ax4.legend()


for folder in os.listdir(input_file):

    if "anchors_" in folder:
        for trajectory in os.listdir(os.path.join(input_file, folder)):
            if plot_solo:
                # Plot protagonist solo

                fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

                for log in os.listdir(os.path.join(input_file, folder)):
                    if "DroneUser_DronePosLog_SimType_0" in log:
                        DataPath = os.path.join(input_file, folder, log)
                        DataPlotter(DataPath, ax1, ax2, ax3, ax4, fig)
                plt.suptitle("Solo flight path: " + str(folder.split("_")[1]))
                plt.show()


            if plot_helped:
                # Plot protagonist with help
                fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

                for log in os.listdir(os.path.join(input_file, folder)):
                    if "DroneUser_DronePosLog_SimType_1" in log:
                        DataPath = os.path.join(input_file, folder, log)
                        DataPlotter(DataPath, ax1, ax2, ax3, ax4, fig)
                plt.suptitle("Helped flight path: " + str(folder.split("_")[1]))
                plt.show()

            if plot_helpers:
                # Plot helper drone trajectories

                fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

                for i in range(N_helpers):
                    DataPath = os.path.join(input_file, folder, "DronePosLog" + str(i) + ".csv")
                    DataPlotter(DataPath, ax1, ax2, ax3, ax4, fig)


                plt.suptitle("Helper flight paths: " + str(folder.split("_")[1]))
                plt.show()




