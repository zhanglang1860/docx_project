import pandas as pd
import numpy as np

basestation = r"C:\Users\Administrator\PycharmProjects\docx_project\chapter\风速风频.xlsx"
basestation1 = r"C:\Users\Administrator\PycharmProjects\docx_project\chapter\风速风频1.txt"

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
data['sd_sd'] = wind_10min_SD / wind_10min
statistics_times_times = data.groupby(by=['sector']).size()
statistics_times_times = statistics_times_times.reset_index(name='times')


def frequency(x):
    return (x / statistics_times_times['times'].sum())


def ti(x):
    return (x + statistics_ti['sd_sd'].std() * 1.28)


statistics_times_times['frequency'] = statistics_times_times['times'].map(frequency)
print(statistics_times_times)
npa = statistics_times_times[((statistics_times_times['frequency']) > 0.1)]
npa_np = np.array(npa[['sector', 'frequency']])
print(npa_np)
result = [i for i in range(0, 21)]
result_np = [i for i in range(0, 21)]
for i in range(0, 21):
    statistics_ti = data.loc[data['wind_speed'] == i + 1]
    # print(i, statistics_ti['sd_sd'].mean(), statistics_ti['sd_sd'].std() * 1.28)
    print("```````````````````")
    statistics_ti_np = np.array(statistics_ti[['sector', 'sd_sd']])
    print("```````````````````")
    statistics_ti_np_f = []
    for j in range(0, len(statistics_ti_np[:, 1])):
        if statistics_ti_np[j, 1] > 0.2 and (statistics_ti_np[j, 0] not in npa_np[:, 0]):
            statistics_ti_np[j, 1] = None
        else:
            statistics_ti_np_f.append(statistics_ti_np[j, 1])

    statistics_ti_np_f = np.array(statistics_ti_np_f)
    print("*******************")
    print("statistics_ti_np" + str(len(statistics_ti_np)))
    print("statistics_ti_np_f"+str(len(statistics_ti_np_f)))
    # statistics_ti = statistics_ti[(statistics_ti['sd_sd'] > 0.2 and np['sector'].isin([statistics_ti['sector']]))]

    # print(statistics_ti_np)

    # result[i] = statistics_ti['sd_sd'].mean() + statistics_ti['sd_sd'].std() * 1.28
    result_np[i] = statistics_ti_np_f.mean() + statistics_ti_np_f.std() * 1.28
    print(result_np[i])
f1 = open(basestation1, 'w')
f1.write(str(result_np))
f1.close()
print()
print("-----------数组写入Excel完成-------------")
