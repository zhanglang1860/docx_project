#coding:utf-8
import datetime
import pandas as pd
import numpy as np
import pickle

#用pandas将时间转为标准格式
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M')
#将时间栏合并,并转为标准时间格式
rawdata = pd.read_csv(r'C:\Users\Administrator\PycharmProjects\untitled\files\00641.csv',parse_dates={'timeline':['Date/Time']},date_parser=dateparse)
# rawdata = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\untitled\files\0064.xlsx',parse_dates={'timeline':['Date/Time']},date_parser=dateparse)

#定义一个将时间转为数字的函数,s为字符串
def datestr2num(s):
    #toordinal()将时间格式字符串转为数字
    # return datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S').toordinal()
    date=datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')+ datetime.timedelta(hours=8)
    return date.timestamp()
x = []
y = []
new_date = []

for i in range(rawdata.shape[0]):
    x_convert = int(datestr2num(str(rawdata.ix[i,0])))
    new_date.append(x_convert)
    y_convert = rawdata.ix[i,1].astype(np.float32)
    x.append(x_convert)
    y.append(y_convert)

x = np.array(x).astype(np.float32)
print(x[2])
"""
"""
print(datetime.datetime.utcfromtimestamp(new_date[0]),'------>>>>>>',y[0])
print(datetime.datetime.utcfromtimestamp(new_date[1]),'------>>>>>>',y[1])
print(datetime.datetime.utcfromtimestamp(new_date[2]),'------>>>>>>',y[2])
print(datetime.datetime.utcfromtimestamp(new_date[3]),'------>>>>>>',y[3])
print(datetime.datetime.utcfromtimestamp(new_date[4]),'------>>>>>>',y[4])
print(datetime.datetime.utcfromtimestamp(new_date[5]),'------>>>>>>',y[5])
