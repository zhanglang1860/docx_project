import pandas as pd
import numpy as np


class frequency:

    def __init__(self):
        self.data = pd.DataFrame()

    #
    # def ti(x):
    #     return (x + statistics_ti['sd_sd'].std() * 1.28)
    def frequency_statistics(self, wind_10min_D):
        # wind_10min = data.iloc[:, 1]
        # wind_10min_SD = data.iloc[:, 2]
        # wind_10min_D = data.iloc[:, 3]
        sector = [i for i in range(0, len(wind_10min_D))]

        for i in range(0, len(wind_10min_D)):
            if wind_10min_D[i] < 11.25 or wind_10min_D[i] > 348.75:
                sector[i] = 0
            elif wind_10min_D[i] > 11.25 and wind_10min_D[i] < 33.75:
                sector[i] = 22.5
            elif wind_10min_D[i] > 33.75 and wind_10min_D[i] < 56.25:
                sector[i] = 45
            elif wind_10min_D[i] > 56.25 and wind_10min_D[i] < 78.75:
                sector[i] = 67.5
            elif wind_10min_D[i] > 78.75 and wind_10min_D[i] < 101.25:
                sector[i] = 90
            elif wind_10min_D[i] > 101.25 and wind_10min_D[i] < 123.75:
                sector[i] = 112.5
            elif wind_10min_D[i] > 123.75 and wind_10min_D[i] < 146.25:
                sector[i] = 135
            elif wind_10min_D[i] > 146.25 and wind_10min_D[i] < 168.75:
                sector[i] = 157.5
            elif wind_10min_D[i] > 168.75 and wind_10min_D[i] < 191.25:
                sector[i] = 180
            elif wind_10min_D[i] > 191.25 and wind_10min_D[i] < 213.75:
                sector[i] = 202.5
            elif wind_10min_D[i] > 213.75 and wind_10min_D[i] < 236.25:
                sector[i] = 225
            elif wind_10min_D[i] > 236.25 and wind_10min_D[i] < 258.75:
                sector[i] = 247.5
            elif wind_10min_D[i] > 258.75 and wind_10min_D[i] < 281.25:
                sector[i] = 270
            elif wind_10min_D[i] > 281.25 and wind_10min_D[i] < 303.75:
                sector[i] = 292.5
            elif wind_10min_D[i] > 303.75 and wind_10min_D[i] < 326.25:
                sector[i] = 315
            elif wind_10min_D[i] > 326.25 and wind_10min_D[i] < 348.75:
                sector[i] = 337.5
            else:
                sector[i] = 999
        self.data['sector'] = sector
        # data['sd_sd'] = wind_10min_SD / wind_10min
        self.statistics_times_times = self.data.groupby(by=['sector']).size()
        self.statistics_times_times = self.statistics_times_times.reset_index(name='times')
        return self.statistics_times_times['times']


