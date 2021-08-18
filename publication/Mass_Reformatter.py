import os

publication_folder = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication")
for run_folder in os.listdir(publication_folder):
    if "anchors_" in run_folder:
        print(run_folder)

        Na = int(run_folder.split("_")[1])
        print("Na:", Na)
        N_helpers = int(run_folder.split("_")[3])
        print("Nh:", N_helpers)
        for trajectory in os.listdir(os.path.join(publication_folder, run_folder)):
            if N_helpers == 0:
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog2.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog3.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog4.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog5.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog6.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLog7.csv"))

