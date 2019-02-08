from docxtpl import DocxTemplate, InlineImage
# coding=utf=8
import pymysql
import psycopg2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# db = pymysql.connect(host='localhost', user='root', passwd='Yuwen520', port=3306, db='tur', charset='utf8')

db = psycopg2.connect(host='localhost', user='zhangyicheng', password='12345', port=5432, database='Turbine')

cur = db.cursor()
sql_str = ''
data_name = ('GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'MY100')
# data_name = ('GW3.3-155', 'MY2.5-145', 'MY3.2-145', 'GW140-3.4', 'En2.5-141', 'GW3.0-140', 'En3.0-141')

for i in range(len(data_name)):
    if i == len(data_name) - 1:
        sql_str = "(" + sql_str + '\'%s\')'
    else:
        sql_str = sql_str + '\'%s\','
print(sql_str)

# selectsql = "SELECT * FROM tur_model WHERE tur_type_name in " + "('%s','%s','%s','%s','%s','%s','%s')"
selectsql = "SELECT * FROM power_model WHERE tur_type_name in " + sql_str

cur.execute(selectsql % data_name)
data = cur.fetchall()  # 所有
# for item in data:
#     print(item)
db.close()
data_np = np.array(data)

speed = np.zeros(data_np.shape[1] - 2)

for i in range(0, data_np.shape[1] - 2):
    if i == 0:
        speed[i] = 2.5
    else:
        speed[i] = i + 2
power = data_np[:, 2: data_np.shape[1]].astype('float32')
turbine_model = data_np[:, 1]

print(turbine_model)
#
#
plt.figure(figsize=(7, 4))
for i in range(len(turbine_model)):
    plt.plot(speed, power[i], label=turbine_model[i])
plt.xlim((2.5, 25))
plt.ylim((0.0, 4000.0))
plt.xlabel("Wind speed")
plt.ylabel("Power")
new_ticks = np.linspace(0, 4000, 9)
print(new_ticks)
plt.yticks(new_ticks)
plt.legend(loc='lower right')
# plt.subplots_adjust(left=0.05,right=0.95,wspace=0.25,hspace=0.25,bottom=0.13,top=0.91)

plt.savefig(r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\powers.png')

#
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\docx_project\files\华润template.docx')

context = {}
for i in range(0, 1):
    # if i < 13:
    #     key = 'tbl_contents' + str(i)
    #     value = data_np[:, i + 1]
    #     context[key] = value
    # else:
    #     key = 'tbl_contents' + str(i)
    #     value = data_np[:, i + 4]
    #     context[key] = value
    key = 'myimage' + str(i)
    value = InlineImage(tpl, r'C:\Users\Administrator\PycharmProjects\docx_project\files\results\powers.png')
    context[key] = value
print(context)

tpl.render(context)
tpl.save(r'C:\Users\Administrator\PycharmProjects\docx_project\files\result4.docx')
