# coding=utf=8
import os
import numpy as np
import matplotlib.pyplot as plt
from connect_sql import connect_sql


# def generate_images(save_path, turbine_list):
def generate_images(save_path, power_np, efficiency_np):
    png_box = ('powers', 'efficiency')

    # tur_np, power_np, efficiency_np = connect_sql(*turbine_list)

    speed = np.zeros(power_np.shape[1] - 2)
    for i in range(0, power_np.shape[1] - 2):
        if i == 0:
            speed[i] = 2.5
        else:
            speed[i] = i + 2
    power = power_np[:, 2: power_np.shape[1]].astype('float32')
    efficiency = efficiency_np[:, 2: efficiency_np.shape[1]].astype('float32')

    turbine_power_model = power_np[:, 1]
    turbine_efficiency_model = efficiency_np[:, 1]

    # figure power
    plt.figure(figsize=(5.6, 3.15))
    for i in range(len(turbine_power_model)):
        plt.plot(speed, power[i], label=turbine_power_model[i])
    plt.xlim((2.5, 25))
    plt.ylim((0.0, 4000.0))
    plt.xlabel("Wind speed")
    plt.ylabel("Power")
    new_ticks = np.linspace(0, 4000, 9)
    print(new_ticks)
    plt.yticks(new_ticks)
    plt.legend(loc='lower right')
    plt.subplots_adjust(left=0.115, right=0.965, wspace=0.200, hspace=0.200, bottom=0.145, top=0.96)
    plt.savefig(os.path.join(save_path, '%s.png') % png_box[0])

    # figure efficiency
    plt.figure(figsize=(5.6, 3.15))
    for i in range(len(turbine_efficiency_model)):
        plt.plot(speed, efficiency[i], label=turbine_efficiency_model[i])
    plt.xlim((3, 20))
    plt.ylim((0.0, 0.5))
    plt.xlabel("Wind speed")
    plt.ylabel("efficiency")
    new_ticks = np.linspace(3, 20, 18)
    print(new_ticks)
    plt.xticks(new_ticks)

    new_ticks = np.linspace(0, 0.5, 11)
    print(new_ticks)
    plt.yticks(new_ticks)
    plt.legend(loc='upper right')
    plt.subplots_adjust(left=0.115, right=0.965, wspace=0.200, hspace=0.200, bottom=0.145, top=0.96)
    plt.savefig(os.path.join(save_path, '%s.png') % png_box[1])
