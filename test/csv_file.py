import csv
import os
import pandas as pd
import numpy as np
from collections import Counter
import psycopg2
import xlwt

# path = 'rotor_profile.csv'
# data = pd.read_csv('rotor_profile.csv')
# data_np = np.array(data)
# print(data_np[:, 2])
# num_tur = len(set(data_np[:, 2]))
# num_deg = np.sum(data_np == '   no') + 1
# print(num_tur, num_deg)
# print(set(data_np[:, 2]))
# for tur_items in range(0,num_tur):



def connect_sql_chapter5():
    db = psycopg2.connect(host='localhost', user='zhangyicheng', password='12345', port=5432, database='Turbine')
    cur = db.cursor()
    sql_str = 'vref'

    # 第五章
    selectsql_towerno = "SELECT * FROM windsim03 WHERE  cola='climatologynumber'"
    selectsql_vref = "SELECT * FROM windsim03 WHERE  cola='vref'"
    selectsql_wecsnumber = "SELECT * FROM windsim03 WHERE  cola='wecsnumber'"

    cur.execute(selectsql_towerno)
    data_towerno = cur.fetchall()  # 所有
    cur.execute(selectsql_vref)
    data_vref = cur.fetchall()  # 所有
    cur.execute(selectsql_wecsnumber)
    data_wecsnumber = cur.fetchall()  # 所有
    db.close()
    data_towerno_np = np.array(data_towerno)
    data_vref_np = np.array(data_vref)
    data_wecsnumber_np = np.array(data_wecsnumber)
    return data_towerno_np, data_vref_np, data_wecsnumber_np


data_towerno_np, data_vref_np, data_wecsnumber_np = connect_sql_chapter5()
print(data_towerno_np.shape, data_vref_np.shape, data_wecsnumber_np.shape)

towerno = len(set(data_towerno_np[:, 1]))
print(towerno)
wecsnumber = len(set(data_wecsnumber_np[:, 1]))
print(wecsnumber)
print(data_vref_np[0])
data_towerno_np = data_towerno_np.reshape(towerno, wecsnumber+1, 2)
data_vref_np = data_vref_np.reshape(towerno, wecsnumber+1, 2)

data = np.concatenate((data_towerno_np, data_vref_np), axis=2)
# print(data[0,0,1])

# a, b = input('"输入测风塔的测风塔编号 "+"及测风塔编号对应的风机编号 空格隔开:').split()
# # print(data[int(a) - 1, int(b), 1])
# print("输入测风塔的测风塔编号" + str(a) + "测风塔编号对应的风机编号" + str(b) + "--->输出为%s" % (data[int(a) - 1, int(b), [2,3]]))
data_f=np.zeros([towerno,wecsnumber])
for i in range(0,int(towerno)):
    for j in range(0,int(wecsnumber)):
        data_f[i,j]=data_vref_np[i,j,1]

path=r'C:\Users\Administrator\Desktop\\result1802.xls.'
book = xlwt.Workbook()
#创建表单
sheet1 = book.add_sheet(u'sheet2',cell_overwrite_ok=True)
#按i行j列顺序依次存入表格
for i in range(data_f.shape[0]):
    for j in range(data_f.shape[1]):
        sheet1.write(i,j,data_f[i][j])
#保存文件
book.save(path)

# s = set(data_np[[1], :, 3])
# len(s)  # 得到个数
#
# print(num_deg)
# #
# def getlistnum(li):  # 这个函数就是要对列表的每个元素进行计数
#     name_np = list(li[0, :])
#     value = list(li)
#     # set1 = set(li)
#     dict1 = {}
#     for item in name_np:
#         dict1.update({item: value.count(item)})
#     return dict1
#
#
# zero_col_count = getlistnum(data_np)  # df[0]指列名为0的列，如果你的列名是字符串就要加引号
# print(zero_col_count)

#
# with open(path, 'r', newline='') as file:
#     csvreader = csv.reader(file)
#     # aa = next(csvreader)
#     # print(aa)
#     i = j = 0
#     for row in csvreader:
#         print("ass"+str(row))
#         if i == 1:
#             print(f'i is {i}, j is {j}')
#             print(row)
#         if row[0] != '' and row[0] == '   sector:':
#             j += 1
#             print(f"csv {j} 生成成功")
#         csv_path = os.path.join('/'.join(path.split('/')[:-1]), 'cf/' + str(j) + '.csv')
#         # print('/'.join(path.split('/')[:-1]))
#         # print(csv_path)
#         i += 1
#         # # 不存在此文件的时候，就创建
#         # if not os.path.exists(csv_path):
#         #     with open(csv_path, 'w', newline='') as file:
#         #         csvwriter = csv.writer(file)
#         #         csvwriter.writerow(['image_url'])
#         #         csvwriter.writerow(row)
#         #     i += 1
#         # # 存在的时候就往里面添加
#         # else:
#         #     with open(csv_path, 'a', newline='') as file:
#         #         csvwriter = csv.writer(file)
#         #         csvwriter.writerow(row)
#         #     i += 1
