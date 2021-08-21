"""Collect data for comparison of MHE and EKF with different number of anchors

This script simulates the performance of MHE and EKF on the trajectories
in the data/publication_run folder. For each file, the number of anchors 
is varied between 1-8 for TWR and 2-8 for TDOA. Every number of anchor 
is tested in 10 runs with the anchors chosen randomly for every run.
The position RMSE for both MHE and EKF is recorded in a csv file that
can then be used to generate plots with the 'publication_plots.py' script.
"""

import os
import yaml
import numpy as np
import random
import time

start_time = time.time()

import UWBsim
from UWBsim.airframe.drone import Drone
from UWBsim.utils.uwb_ranging import RangingType, RangingSource
from UWBsim.simulation import UWBSimulation, SimulationParams

# Script settings SEE LINE 58
#N_helpers = 4
#Na = 4
#InputNr = 0
#simulation_type = 1

runs_per_traj_file = 5
mode = 'tdoa'
data_folder = os.path.join(UWBsim.DATA_DIR)
anchor_file = os.path.join(UWBsim.BASE_DIR, 'anchor_positions.yaml')
publication_folder = os.path.dirname(os.path.realpath(__file__))

# Set Estimator parameters
params = SimulationParams()
params.estimators.ekf.enable = True
params.estimators.ekf.rate = 100

params.drone.altitude_enable = True

if mode == 'twr':
    n_anchors = [1, 2, 3, 4, 5, 6, 7, 8]
    params.ranging.rtype = RangingType.TWR
    params.estimators.ekf.outlierThreshold = 1500
elif mode == 'tdoa':
    n_anchors = [2, 3, 4, 5, 6, 7, 8]
    params.ranging.rtype = RangingType.TDOA
    params.estimators.ekf.outlierThreshold = 25

with open(anchor_file) as f:
    positions = yaml.safe_load(f)
    params.ranging.anchor_positions = []
    for key, pos in positions.items():
        i = int(key)
        params.ranging.anchor_positions.append([pos['x'], pos['y'], pos['z']])

params.ranging.source = RangingSource.LOG



i = 0
publication_folder_hip = os.path.join(publication_folder, str(mode) + str(i))
while os.path.isdir(publication_folder_hip):
    publication_folder_hip = os.path.join(publication_folder, str(mode) + str(i))
    i += 1
output_file = os.path.join(publication_folder_hip, 'runs_data.csv'.format(mode))
drone_log_file_directory = os.path.join(publication_folder_hip, "DronePosLog")


"""
# Save parameters for later reference
settings_file = output_file.split('.')[0] + '_settings.yaml'
with open(settings_file, 'w') as f:
    yaml.dump(params, f)
"""

# Global variables for error calculation and drone tracking
# mhe_error_sum2 = np.array([0.0,0.0,0.0])
ekf_error_sum2 = np.array([0.0, 0.0, 0.0])
error_count = 0
ekf_error_count = 0
drone_full_x_log = np.empty((60000, 7))


###drone_full_x_log2 = np.empty((0,4))


def data_callback(drone: Drone):
    """Record the simulation output in the scripts global variables

    This function is passed to the simulation and is called at every 
    simulation step. It records the true and estimated states of MHE
    and EKF in the scripts global variables, so that the performance
    can be calculated at the end of the simulation. 
    """
    global error_count, ekf_error_count, ekf_error_sum2, drone_full_x_log  ###, drone_full_x_log2#, mhe_error_sum2
    # wait a moment before starting error calculation (calibration)
    if drone.time > 1.0:
        x = drone.state_true.x[0]
        y = drone.state_true.x[1]
        z = drone.state_true.x[2]

        drone_flight_info = np.array(
            [np.hstack((drone.time, drone.state_estimate["ekf"].x[0:3], drone.state_true.x[0:3]))])
        ###print("EKF X", drone.state_estimate["ekf"].x)
        ###print(np.transpose(drone.estimators["ekf"].xi[0:3]))
        drone_full_x_log[error_count] = drone_flight_info
        # drone_full_x_log = np.append(drone_full_x_log, drone_flight_info, axis=0)
        #######print(drone_full_x_log[-1])
        ###drone_full_x_log2 = np.append(drone_full_x_log2, np.array(drone.time, np.transpose(drone.estimators["ekf"].xi[0:3])), axis=0)

        error_count += 1

        """
        if drone.estimator_isEnabled['mhe']:
            mhe_error_sum2[0] += (x - drone.state_estimate['mhe'].x[0])**2
            mhe_error_sum2[1] += (y - drone.state_estimate['mhe'].x[1])**2
            mhe_error_sum2[2] += (z - drone.state_estimate['mhe'].x[2])**2
        """
        if drone.estimator_isEnabled['ekf'] and z > 0.1:
            ekf_error_count += 1
            ekf_error_sum2[0] += (x - drone.state_estimate['ekf'].x[0]) ** 2
            ekf_error_sum2[1] += (y - drone.state_estimate['ekf'].x[1]) ** 2
            ekf_error_sum2[2] += (z - drone.state_estimate['ekf'].x[2]) ** 2




for input_file in os.listdir(publication_folder):
    if "anchors_" in input_file:
        Na = int(input_file[8])
        N_helpers = int(input_file[-7])

        if N_helpers == 0:
            simulation_type = 0
        else:
            simulation_type = 1

        params.ranging.anchor_enable = [Na > 0, Na > 4, Na > 1, Na > 5,
                                        Na > 6, Na > 2, Na > 7, Na > 3]

        for folder in os.listdir(input_file):
            print('Reading from: {}'.format(os.path.join(input_file, folder)))

            print(os.path.join(data_folder, folder + ".csv"))
            params.drone.logfile = os.path.join(data_folder, folder + ".csv")
            params.drone.helper_file = os.path.join(input_file, folder)


            params.ranging.simulation_type = simulation_type

            f_out = open(os.path.join(input_file, folder, "DroneUser_runs_data" + str(simulation_type)) + ".csv", "w")
            f_out.write('log, anchors, run, ekf_tot, ekfX, ekfY, ekfZ, logfile\n')


            for run in range(runs_per_traj_file):


                # anchor_idx_en = random.sample(range(8), Na)
                # for a_idx in range(Na):
                #    params.ranging.anchor_enable[a_idx] = True
                if simulation_type == 0:
                    params.name = folder + '_SOLO' + '_r' + str(run)
                elif simulation_type == 1:
                    params.name = folder + '_h' + str(N_helpers) + '_r' + str(run)
                # Reset error calculation
                error_count = 0
                # mhe_error_sum2[0] = 0
                # mhe_error_sum2[1] = 0
                # mhe_error_sum2[2] = 0
                ekf_error_sum2[0] = 0
                ekf_error_sum2[1] = 0
                ekf_error_sum2[2] = 0

                # Reset drone x array
                drone_full_x_log = np.empty((60000, 7))
                ###drone_full_x_log2 = np.empty((0,4))

                # Run simulation
                sim = UWBSimulation(params, NotImplemented, data_callback)
                try:
                    sim.start_sim()
                    # mheX = np.sqrt(mhe_error_sum2[0]/error_count)
                    # mheY = np.sqrt(mhe_error_sum2[1]/error_count)
                    # mheZ = np.sqrt(mhe_error_sum2[2]/error_count)
                    ekfX = np.sqrt(ekf_error_sum2[0] / error_count)
                    ekfY = np.sqrt(ekf_error_sum2[1] / error_count)
                    ekfZ = np.sqrt(ekf_error_sum2[2] / error_count)
                except AssertionError:
                    # One of the estimators failed, try both individually

                    # EKF only
                    params.estimators.mhe.enable = False
                    error_count = 0
                    ekf_error_sum2[0] = 0
                    ekf_error_sum2[1] = 0
                    ekf_error_sum2[2] = 0
                    try:
                        sim = UWBSimulation(params, NotImplemented,
                                            data_callback)
                        sim.start_sim()
                        ekfX = np.sqrt(ekf_error_sum2[0] / error_count)
                        ekfY = np.sqrt(ekf_error_sum2[1] / error_count)
                        ekfZ = np.sqrt(ekf_error_sum2[2] / error_count)

                    except AssertionError:
                        ekfX = np.inf
                        ekfY = np.inf
                        ekfZ = np.inf

                    finally:
                        # params.estimators.mhe.enable = True
                        pass

                # Calculate performance and write to output file
                # mhe_tot = np.sqrt(mheX**2 + mheY**2 + mheZ**2)
                ekf_tot = np.sqrt(ekfX ** 2 + ekfY ** 2 + ekfZ ** 2)



                f_out.write('{}, {}, {}, \
                {:.5f}, {:.4f}, {:.4f}, {:.4f}, {}\n'.format(
                    folder, Na, run, ekf_tot, ekfX, ekfY, ekfZ, os.path.join(input_file, folder)
                ))

                drone_full_x_log = drone_full_x_log[~np.all(drone_full_x_log == 0, axis=1)]

                np.savetxt(os.path.join(input_file, folder, "DroneUser_DronePosLog_SimType_" + str(simulation_type) + "_r" + str(run) + ".csv"), drone_full_x_log,
                           header="time, estX, estY, estZ, trueX, trueY, trueZ", comments="", delimiter=",")
                ###np.save(os.path.join("C:\\Users\\Kian Heus\\PycharmProjects\\numpytester\\savehere",
                ###"x_array" + str(Na) + str(run) + "BOO"), drone_full_x_log2)

                print("RUNTIME:", time.time() - start_time)
            f_out.close()
