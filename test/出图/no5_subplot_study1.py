#-*- coding:utf-8 -*-  

# 设置中文utf-8解释环境标识。
# No例2:相关性分析方法示例及代码详解,熟悉一元回归线性相关的计算及图示显示。
# 研究测风塔与测风塔之间,同一座测风塔之间10m,30m,50m,70m不同测层的10min平均风速之间的相关性。
# 研究测风塔轮毂高度处测层70m高度10min风速与气象站10min平均风速之间的相关性。
# 熟悉数据框的时间格式设置函数  to_datatime()函数
# 熟悉数据框的设定索引的函数 set_index()函数
# 熟悉Pandas提取某一段时间序列索引段的数据的方法：data1 = data['2011/3/13 00:00':'2012/3/14 00:00']
# 研究设定 一元线性回归.熟悉一元线性回归的X矩阵转换方法data[:,np.newaxis]
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd  #导入pandas包
import pylab as pl
import numpy as np 
import datetime
from datetime import datetime

mpl.rcParams["font.sans-serif"]=["SimHei"] # 设置坐标轴标识字符串中的中文标识的字体为黑体
mpl.rcParams['axes.unicode_minus'] = False # 不使用默认的unicode minus模式来处理坐标轴轴线的刻度标签为负数的情况。

import math
import scipy 
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression 

#导入测风数据的数据文件speedData1.csv.
data = pd.read_csv("speedData1.csv") #pandas 中输入EXCEL表格分隔数据CSV格式的方法

data['Date']= pd.to_datetime(data['Date'],format='%Y/%m/%d %H:%M') 
#设定数据框中的Date时间列表的数据为时间数据格式(包括 Y m d H M S)。
data = data.set_index('Date') # 设定数据的时间序列索引'Date'
data1 = data['2011/3/13 00:00':'2012/3/14 00:00']
#根据时间序列的索引格式，调取‘2011/3/13 00:00’至‘2012/3/14 00:00’时间段整一年的数据，组成一个新的数据框data1.
#1
data1_1_direction = data1[(data1['CH7Avg'] > 0) & (data1['CH7Avg'] < 90)]
speed_1_x = data1_1_direction['CH3Avg']
speed_1_y = data1_1_direction['CH13Avg']
X_speed_1_x = speed_1_x[:,newaxis]
#2
data1_2_direction = data1[(data1['CH7Avg'] > 90) & (data1['CH7Avg'] < 180)]
speed_2_x = data1_2_direction['CH3Avg']
speed_2_y = data1_2_direction['CH13Avg']
X_speed_2_x = speed_2_x[:,newaxis]
#3
data1_3_direction = data1[(data1['CH7Avg'] > 180) & (data1['CH7Avg'] < 270)]
speed_3_x = data1_3_direction['CH3Avg']
speed_3_y = data1_3_direction['CH13Avg']
X_speed_3_x = speed_3_x[:,newaxis]

#4
data1_3_direction = data1[(data1['CH7Avg'] > 270) & (data1['CH7Avg'] < 360)]
speed_3_x = data1_3_direction['CH3Avg']
speed_3_y = data1_3_direction['CH13Avg']
X_speed_3_x = speed_3_x[:,newaxis]





print(data1_n_direction.head())

fig1=plt.figure(figsize=(10,10))
fig1,ax = plt.subplots(2,2)#以4个扇区为例来画一张有4幅子图的图形
#subplot(221),2表示2行,2表示2列,1标识排下来的第一张图.
	
ax1 = plt.subplot(221)
#调用输入数据自定义函数,按风向区间取收据集,增加变换列矩阵,返回X,y




	
#subplot(222),2表示2行,2表示2列,2表示排下来的第2张图,画第2张子图.
ax2 = plt.subplot(222)





	
ax3 = plt.subplot(223)





	
ax4 = plt.subplot(224)





