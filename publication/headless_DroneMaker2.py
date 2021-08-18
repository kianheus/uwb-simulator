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
import csv

start_time = time.time()

import UWBsim
from UWBsim.airframe.drone import Drone
from UWBsim.utils.uwb_ranging import RangingType, RangingSource
from UWBsim.simulation import UWBSimulation, SimulationParams

# Script settings
N_helpers = 5
#Na = 5
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

params.ranging.source = RangingSource.GENERATE_HT_CAUCHY
params.ranging.simulation_type = 0




# Global variables for error calculation and drone tracking
# mhe_error_sum2 = np.array([0.0,0.0,0.0])
ekf_error_sum2 = np.array([0.0, 0.0, 0.0])
error_count = 0
drone_full_x_log = np.empty((60000, 7))


###drone_full_x_log2 = np.empty((0,4))


def data_callback(drone: Drone):
    """Record the simulation output in the scripts global variables

    This function is passed to the simulation and is called at every
    simulation step. It records the true and estimated states of MHE
    and EKF in the scripts global variables, so that the performance
    can be calculated at the end of the simulation.
    """
    global error_count, ekf_error_sum2, drone_full_x_log  ###, drone_full_x_log2#, mhe_error_sum2
    # wait a moment before starting error calculation (calibration)
    if drone.time > 1.0:
        x = drone.state_true.x[0]
        y = drone.state_true.x[1]
        z = drone.state_true.x[2]

        drone_flight_info = np.array(
            [np.hstack((drone.time, drone.state_estimate["ekf"].x[0:3], drone.state_true.x[0:3]))])
        drone_full_x_log[error_count] = drone_flight_info

        error_count += 1

        if drone.estimator_isEnabled['ekf']:
            ekf_error_sum2[0] += (x - drone.state_estimate['ekf'].x[0]) ** 2
            ekf_error_sum2[1] += (y - drone.state_estimate['ekf'].x[1]) ** 2
            ekf_error_sum2[2] += (z - drone.state_estimate['ekf'].x[2]) ** 2


for Na in range(2, 4):
    for N_helpers in range(8,9):
        # iterate through all logs
        traj_names = []

        i = 0
        publication_folder_main = os.path.join(publication_folder, "anchors_" + str(Na) + "_helpers_" + str(
            N_helpers) + "_run_" + str(i))
        while os.path.isdir(publication_folder_main):
            publication_folder_main = os.path.join(publication_folder, "anchors_" + str(Na) + "_helpers_" + str(
            N_helpers) + "_run_" + str(i))
            i += 1

        for f in os.listdir(data_folder):
            if not mode in f:
                continue
            elif 'BAD' in f:
                continue
            elif f.startswith('.'):
                continue

            # Create human readable name for trajectories
            name = f.split('.')[0]
            name = name.split('_')[-2]
            if 'twr' in f:
                name = 'twr_' + name
            elif 'tdoa' in f:
                name = 'tdoa_' + name

            index = 0

            while True:
                tmp = name + '_' + str(index)
                if tmp in traj_names:
                    index += 1
                else:
                    name = tmp
                    traj_names.append(name)
                    break

            # Set Logfile for run
            params.drone.logfile = os.path.join(data_folder, f)

            # Create unique output file
            output_file = os.path.join(publication_folder,
                                       name + '_anchors.csv'.format(mode))


            publication_folder_shape = os.path.join(publication_folder_main, name)
            output_file = os.path.join(publication_folder_shape, 'runs_data.csv'.format(mode))
            drone_log_file_directory = os.path.join(publication_folder_shape, "DronePosLog")

            if not os.path.isdir(publication_folder_main):
                os.makedirs(publication_folder_main)
            os.makedirs(publication_folder_shape)

            # Save parameters for later reference
            settings_file = output_file.split('.')[0] + '_settings.yaml'
            with open(settings_file, 'w') as f:
                yaml.dump(params, f)

            with open(output_file, 'w') as f_out:
                print('Writing to: {}'.format(output_file))
                # Write output file header
                f_out.write('log, anchors, run, ekf_tot, ekfX, \
                    ekfY, ekfZ, logfile\n')


                print("Na =", Na, "n_anchors =", n_anchors)
                # params.estimators.mhe.alpha = mhe_alphas[idx]

                for helper in range(N_helpers):

                    # Special case for 8 drones: where the grid is
                    # 0|1|2
                    # 3|*|4
                    # 5|6|7
                    if N_helpers == 8:
                        params.drone.offset = [0,0,0]
                        if helper <= 2:
                            params.drone.offset[1] = 1
                        elif helper >= 5:
                            params.drone.offset[1] = -1
                        if helper == 0 or helper == 3 or helper == 5:
                            params.drone.offset[0] = -1
                        elif helper == 2 or helper == 4 or helper == 7:
                            params.drone.offset[0] = 1
                    elif N_helpers == 5:
                        params.drone.offset = [0, 0, 0]
                        if helper <= 2:
                            params.drone.offset[1] = 1
                        if helper == 0 or helper == 3:
                            params.drone.offset[0] = -1
                        elif helper == 2 or helper == 4:
                            params.drone.offset[0] = 1
                    # General case, where helper drones form a circle around the protagonist
                    else:
                        params.drone.offset = [1 * np.cos((helper) * 2 * np.pi / (N_helpers)),
                                                1 * np.sin((helper) * 2 * np.pi / (N_helpers)), 0]
                    print("Drone offset:", params.drone.offset)
                    params.ranging.anchor_enable = [Na>0, Na>4, Na>1, Na>5,
                                                    Na>2, Na>6, Na>3, Na>7]

                    # anchor_idx_en = random.sample(range(8), Na)
                    # for a_idx in range(Na):
                    #    params.ranging.anchor_enable[a_idx] = True
                    params.name = name + '_a' + str(Na) + '_r' + str(helper)
                    # Reset error calculation
                    error_count = 0
                    ekf_error_sum2[0] = 0
                    ekf_error_sum2[1] = 0
                    ekf_error_sum2[2] = 0

                    # Reset drone x array
                    drone_full_x_log = np.empty((60000, 7))

                    # Run simulation
                    sim = UWBSimulation(params, NotImplemented, data_callback)
                    try:
                        sim.start_sim()
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
                        name, Na, helper, ekf_tot, ekfX, ekfY, ekfZ, params.drone.logfile
                    ))

                    drone_full_x_log = drone_full_x_log[~np.all(drone_full_x_log == 0, axis=1)]

                    np.savetxt(os.path.join(drone_log_file_directory + str(helper) + ".csv"), drone_full_x_log,
                               header="time, estX, estY, estZ, trueX, trueY, trueZ", comments="", delimiter=",")

                    print("RUNTIME:", time.time() - start_time)






