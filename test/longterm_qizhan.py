#coding:utf-8
import datetime
import pandas as pd
import numpy as np
import re
import pickle
longdate_np = []
hsplit_np=[]
#用pandas将时间转为标准格式
dateparse = lambda dates: pd.datetime.strptime(dates,'%d/%m/%Y %H:%M')
#将时间栏合并,并转为标准时间格式
# rawdata = pd.read_csv('53787 气站数据.csv',parse_dates={'timeline':['date','(UTC)']},date_parser=dateparse)
rawdata = pd.read_csv(r'C:\Users\Administrator\PycharmProjects\untitled\files\53787.csv',
                      header=None,names=['区站号','纬度','经度','观测场海拔高度',
                                         '年','月','日','平均风速','最大风速',
                                         '最大风速的风向','极大风速','极大风速的风向',
                                         'other1','other2','other3','other4','other5'])

longdate_np=np.array(rawdata)
print(longdate_np.shape)
hsplit_np=np.hsplit(longdate_np, (4,7))

test=re.sub('[\[\]]', '', np.array_str(hsplit_np[1][0]))

print(test)

# date_number = datetime.datetime.strptime(str(hsplit_np[1][0]&'-'&hsplit_np[2][0]&'-'&hsplit_np[3][0])
#                                          ,'%Y-%m-%d').timestamp()
#
# print(datetime.datetime.utcfromtimestamp(date_number),'------>>>>>>',date_number)



# #定义一个将时间转为数字的函数,s为字符串
# def datestr2num(s):
#     #toordinal()将时间格式字符串转为数字
#     return datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S').toordinal()
#
# x = []
# y = []
# new_date = []
#
# for i in range(rawdata.shape[0]):
#     x_convert = int(datestr2num(str(rawdata.ix[i,0])))
#     new_date.append(x_convert)
#     y_convert = rawdata.ix[i,1].astype(np.float32)
#     x.append(x_convert)
#     y.append(y_convert)
#
# x = np.array(x).astype(np.float32)
#
# """
# with open('price.pickle','wb') as f:
#     pickle.dump((x,y),f)
# """
# print(datetime.datetime.fromordinal(new_date[0]),'------>>>>>>',new_date[0])
# print(datetime.datetime.fromordinal(new_date[10]),'------>>>>>>',new_date[10])
# print(datetime.datetime.fromordinal(new_date[20]),'------>>>>>>',new_date[20])
# print(datetime.datetime.fromordinal(new_date[30]),'------>>>>>>',new_date[30])
# print(datetime.datetime.fromordinal(new_date[40]),'------>>>>>>',new_date[40])
# print(datetime.datetime.fromordinal(new_date[50]),'------>>>>>>',new_date[50])
