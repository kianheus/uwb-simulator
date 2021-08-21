import csv
import matplotlib.pyplot as plt
import numpy as np
import os

input_file = os.path.join("C:\\Users\\Kian Heus\\Documents\\GitHub\\uwb-simulator\\publication\\anchors_2_helpers_0_run_0\\tdoa_hourglass_0")

PlotDataReader = csv.reader(open(input_file))
Data_Array = np.ndarray((len(open(input_file).readlines()) - 1, 7))

for index, row in enumerate(PlotDataReader):
    Data_Array[index] = np.array([[float(i) for i in row]])

plt.plot(Data_Array[:, 4], Data_Array[:, 5], label="ot")
plt.show()