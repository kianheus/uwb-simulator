import os
import shutil

publication_folder = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication")
for source in os.listdir(os.path.join(publication_folder)):
    if "anchors_" in source:
        for i in range(0,8):
            cutofftext = source[:-7]
            endofftext = source[-6:]
            print(cutofftext)
            print(endofftext)
            dest = os.path.join(os.path.join(publication_folder, cutofftext + str(i) + endofftext))
            destination = shutil.copytree(os.path.join(publication_folder, source), os.path.join(publication_folder, dest))