import pandas as pd
import numpy as np

basestation = r"C:\Users\Administrator\PycharmProjects\docx_project\chapter\阵风系数.xlsx"
basestation1 = r"C:\Users\Administrator\PycharmProjects\docx_project\chapter\阵风系数1.xlsx"

data = pd.read_excel(basestation)

wind_10min = data.iloc[:, 1]
wind_3s = data.iloc[:, 3]
data['wind_10min_3s'] = wind_3s / wind_10min
row = 0

result_mod = len(wind_10min) % 6
result_int = len(wind_10min) // 6

wind_10min_np = np.array(wind_10min)
wind_3s_np = np.array(wind_3s)

wind_10min_re = wind_10min_np[0: 6]
wind_3s_re = wind_3s_np[0: 6]

#
for i in range(1, int(len(wind_10min_np))):
    if i < len(wind_10min_np) - 6:
        wind_10min_re = np.vstack((wind_10min_re, wind_10min_np[i: i + 6]))
        wind_3s_re = np.vstack((wind_3s_re, wind_3s_np[i: i + 6]))
    else:
        wind_10min_re = np.vstack((wind_10min_re, np.zeros(6)))
        wind_3s_re = np.vstack((wind_3s_re, np.zeros(6)))

wind_10min_re_f = wind_10min_re.T
wind_3s_re_f = wind_3s_re.T

print("-----------数组生成完成-------------")
# wind_10min_np = wind_10min_np[0:len(wind_10min) - result_mod]
# wind_3s_np = wind_3s_np[0:len(wind_3s_np) - result_mod]

wind_10min_1h = wind_10min_np
wind_3s_1h = wind_3s_np

for i in range(0, int(len(wind_10min_re_f[1]))):
    if i < int(len(wind_10min_re_f[1])) - 6:
        wind_10min_1h[i] = np.max(wind_10min_re_f[:, i], axis=0) / np.mean(wind_10min_re_f[:, i], axis=0)
        wind_3s_1h[i] = np.max(wind_3s_re_f[:, i], axis=0) / np.mean(wind_10min_re_f[:, i], axis=0)
    else:
        wind_10min_1h[i] = 0
        wind_3s_1h[i] = 0
print("-----------数组计算完成-------------")
print(wind_10min_1h, wind_3s_1h)

data['wind_10min_1h'] = wind_10min_1h
data['wind_3s_1h'] = wind_3s_1h

k = data.sort_values(by="Speed 80 m B [m/s]", ascending=False)
print(k)
k_10min_1h = k.iloc[0:100]['wind_10min_1h'].mean()
k_3s_1h = k.iloc[0:100]['wind_3s_1h'].mean()
data['k_10min_1h'] = k_10min_1h
data['k_3s_1h'] = k_3s_1h

data.to_excel(basestation1, 'page_1', float_format='%.5f')  # float_format 控制精度

print()
print("-----------数组写入Excel完成-------------")
# wind_mean_10min = np.mean(wind_10min_re, axis=1)
# wind_max_10min = np.max(wind_10min_re, axis=1)
# wind_mean_3s = np.mean(wind_3s_np_re, axis=1)
# wind_max_3s = np.max(wind_3s_np_re, axis=1)

#
# print(wind_mean_10min,wind_mean_10min.shape)
# print(wind_max_10min,wind_max_10min.shape)

# wind_10min_1h = wind_max_10min / wind_mean_10min
# wind_3s_1h = wind_max_3s / wind_mean_3s

# row = 0
# result_10min_1h = wind_10min
# result_3s_1h = wind_10min
# print(data.iloc[row:row + 6, 3].max())

# for row in range(0, len(wind_10min)):
#     print(row)
#     if row < len(wind_10min) - 6:
#         result_10min_1h[row] = data.iloc[row:row + 6, 1].max() / data.iloc[row:row + 6, 1].mean()
#         result_3s_1h[row] = data.iloc[row:row + 6, 3].max() / data.iloc[row:row + 6, 3].mean()
#     else:
#         result_10min_1h[row] = 0
#         result_3s_1h[row] = 0
# data['wind_10min_1h'] = result_10min_1h
# data['wind_3s_1h'] = result_3s_1h
# print(result_10min_1h, result_3s_1h)
