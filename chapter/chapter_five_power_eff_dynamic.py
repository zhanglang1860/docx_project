# coding=utf=8
import os
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from docxtpl import DocxTemplate, InlineImage

db = psycopg2.connect(host='localhost', user='zhangyicheng', password='12345', port=5432, database='Turbine')

cur = db.cursor()
sql_str = ''
data_name = ('GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'En2.5-141')

for i in range(len(data_name)):
    if i == len(data_name) - 1:
        sql_str = "(" + sql_str + '\'%s\')'
    else:
        sql_str = sql_str + '\'%s\','

selectsql_power = "SELECT * FROM power_model WHERE tur_type_name in " + sql_str
selectsql_efficiency = "SELECT * FROM efficiency_model WHERE tur_type_name in " + sql_str

cur.execute(selectsql_power % data_name)
data_power = cur.fetchall()  # 所有
cur.execute(selectsql_efficiency % data_name)
data_efficiency = cur.fetchall()  # 所有
db.close()
data_power_np = np.array(data_power)
data_efficiency_np = np.array(data_efficiency)

print(data_efficiency_np)

speed = np.zeros(data_power_np.shape[1] - 2)

for i in range(0, data_power_np.shape[1] - 2):
    if i == 0:
        speed[i] = 2.5
    else:
        speed[i] = i + 2
power = data_power_np[:, 2: data_power_np.shape[1]].astype('float32')
efficiency = data_efficiency_np[:, 2: data_efficiency_np.shape[1]].astype('float32')

turbine_power_model = data_power_np[:, 1]
turbine_efficiency_model = data_efficiency_np[:, 1]

#
#
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
plt.savefig(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\powers.png')
#
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
plt.savefig(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\efficiency.png')

tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\CR_chapter5_template.docx')
png_box = ('powers', 'efficiency')
path = r"C:\Users\Administrator\PycharmProjects\docx_project\files\results"

context = {}
for i in range(0, 2):
    key = 'myimage' + str(i)
    value = InlineImage(tpl, os.path.join(path, '%s.png') % png_box[i])
    context[key] = value
print(context)

tpl.render(context)
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\result1.docx')
