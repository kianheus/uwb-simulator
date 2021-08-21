import os




publication_folder = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication")
for run_folder in os.listdir(publication_folder):
    if "anchors_" in run_folder:
        print(run_folder)

        Na = int(run_folder.split("_")[1])
        N_helpers = int(run_folder.split("_")[3])
        for trajectory in os.listdir(os.path.join(publication_folder, run_folder)):

            for index, log in enumerate(os.listdir(os.path.join(publication_folder, run_folder, trajectory))):
                if "Log" in log and not N_helpers == 8:
                    os.rename(os.path.join(publication_folder, run_folder, trajectory, log),
                              os.path.join(publication_folder, run_folder, trajectory,
                                           "DronePosLog" + chr(index + 65) + ".csv"))
                    # Inverse
                    #os.rename(os.path.join(publication_folder, run_folder, trajectory, log),
                              #os.path.join(publication_folder, run_folder, trajectory, "DronePosLog" + str(index) + ".csv"))
                    print(log)
            if N_helpers == 7:
                print()
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
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"))
            if N_helpers == 6:
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog2.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog3.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog4.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog5.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"))
            if N_helpers == 5:
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog2.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog3.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog4.csv"))
            if N_helpers == 4:
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog2.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog3.csv"))
            if N_helpers == 3:
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog2.csv"))
            if N_helpers == 2:
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog1.csv"))
            if N_helpers == 1:
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"))
                os.rename(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"),
                          os.path.join(publication_folder, run_folder, trajectory, "DronePosLog0.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"))
            if N_helpers == 0:
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogA.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogB.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogC.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogD.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogE.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogF.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogG.csv"))
                os.remove(os.path.join(publication_folder, run_folder, trajectory, "DronePosLogH.csv"))

