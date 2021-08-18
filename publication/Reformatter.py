import os

publication_folder = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication")
for run_folder in os.listdir(publication_folder):
    if "anchors_" in run_folder:
        print(run_folder)

        Na = int(run_folder.split("_")[1])
        print("Na:", Na)
        N_helpers = int(run_folder.split("_")[3])
        print("Nh:", N_helpers)
        if N_helpers == 8:
            for trajectory in os.listdir(os.path.join(publication_folder, run_folder)):
                """
                Do this shit to get them to letters
                
                for index, log in enumerate(os.listdir(os.path.join(publication_folder, run_folder, trajectory))):
                    if "Log" in log:
                        os.rename(os.path.join(publication_folder, run_folder, trajectory, log),
                                  os.path.join(publication_folder, run_folder, trajectory, "DronePosLog" + chr(index+65) + ".csv"))
                        print(log)
                """

                """
                Do this shit if you have them in letters
                
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog2.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog7.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog3.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog6.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog5.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog4.csv"))
                """
                pass