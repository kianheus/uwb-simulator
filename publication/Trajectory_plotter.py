"""
Hello poppet


"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import os

input_file = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication")

def TrajectoryPlotter(DataPath, ax1, ax2, ax3, ax4, fig, run):
    PlotDataReader = csv.reader(open(DataPath))
    Data_Line = next(PlotDataReader)
    Data_Array = np.ndarray((len(open(DataPath).readlines()) - 1, 7))

    for index, row in enumerate(PlotDataReader):
        Data_Array[index] = np.array([[float(i) for i in row]])

    if run == 0:
        ax1.plot(Data_Array[:, 4], Data_Array[:, 5], label="ot")
    ax1.plot(Data_Array[:, 1], Data_Array[:, 2], label="ekf" + str(run), alpha=0.2)
    ax1.set_title("2D top view")
    ax1.legend()

    if run == 0:
        ax2.plot(Data_Array[:, 0], Data_Array[:, 4], label="ot")
    ax2.plot(Data_Array[:, 0], Data_Array[:, 1], label="ekf" + str(run), alpha=0.2)
    ax2.set_title("x-pos vs time")
    # ax2.scatter(Data_Array[:,0], Data_Array[:,1])
    ax2.legend()

    if run == 0:
        ax3.plot(Data_Array[:, 0], Data_Array[:, 5], label="ot")
    ax3.plot(Data_Array[:, 0], Data_Array[:, 2], label="ekf" + str(run), alpha=0.2)
    ax3.set_title("y-pos vs time")
    # ax3.scatter(Data_Array[:,0], Data_Array[:,2])
    ax3.legend()

    if run == 0:
        ax4.plot(Data_Array[:, 0], Data_Array[:, 6], label="ot")
    ax4.plot(Data_Array[:, 0], Data_Array[:, 3], label="ekf" + str(run), alpha=0.2)
    ax4.set_title("z-pos vs time")
    ax4.legend()



plot_helped = False
plot_helpers = True

if plot_helped:
    # Plot protagonist with help

    for folder_index, folder in enumerate(os.listdir(input_file)):
        if "run_2" in folder:
            Na = int(folder[8])
            N_helpers = int(folder[-7])
            for log in os.listdir(os.path.join(input_file, folder)):
                if "hourglass" in log:
                    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
                    for file in os.listdir(os.path.join(input_file, folder, log)):
                        show = False
                        if "DroneUser_DronePosLog_SimType_" in file:
                            run = int(file[-5])
                            DataPath = os.path.join(input_file, folder, log, file)
                            TrajectoryPlotter(DataPath, ax1, ax2, ax3, ax4, fig, run)
                            plt.suptitle("Helped flight path: " + str(log.split("_")[1] + ", Na=" + str(Na) + ", Nh=" + str(N_helpers) + ", run=" + file[-5]))
                            show = True
                    plt.show()
                    plt.close()

if plot_helpers:
    # Plot helper drone trajectories

    for folder_index, folder in enumerate(os.listdir(input_file)):
        if "run_2" in folder:
            Na = int(folder[8])
            N_helpers = int(folder[-7])
            for log in os.listdir(os.path.join(input_file, folder)):
                if "hourglass" in log:
                    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
                    for file in os.listdir(os.path.join(input_file, folder, log)):
                        show = False
                        if "DronePosLog" in file and not "DroneUser" in file:
                            run = int(file[-5])
                            DataPath = os.path.join(input_file, folder, log, file)
                            TrajectoryPlotter(DataPath, ax1, ax2, ax3, ax4, fig, run)
                            plt.suptitle("Helper flight paths: " + str(
                                log.split("_")[1] + ", Na=" + str(Na) + ", Nh=" + str(N_helpers)))
                            show = True
                    plt.show()

