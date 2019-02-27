import pandas as pd
import numpy as np

basestation = r"C:\Users\Administrator\PycharmProjects\docx_project\chapter\风速风频2.xlsx"
basestation1 = r"C:\Users\Administrator\PycharmProjects\docx_project\chapter\风速风频1.xlsx"

data = pd.read_excel(basestation)

wind_10min = data.iloc[:, 1]
wind_10min_SD = data.iloc[:, 2]
wind_10min_D = data.iloc[:, 3]
sector = [i for i in range(0, len(wind_10min))]

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
data['sector'] = sector

gp = data.groupby(by=['sector'])
ne=gp.size()
ne=ne.reset_index(name='times')
print(ne['times'].sum())

# for i in range(0, len(wind_10min_D)):
#     fu[i]=
#     wind_10min_D[i]