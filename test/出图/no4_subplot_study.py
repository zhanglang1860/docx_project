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
data = pd.read_csv("speedData1.csv") #pandas 中输入EXCEL表格分隔数据CSV格式的方法
data['Date']= pd.to_datetime(data['Date'],format='%Y/%m/%d %H:%M') 
#设定数据框中的Date时间列表的数据为时间数据格式(包括 Y m d H M S)。
data = data.set_index('Date') # 设定数据的时间序列索引'Date'
data1 = data['2011/3/13 00:00':'2012/3/14 00:00']
#根据时间序列的索引格式，调取‘2011/3/13 00:00’至‘2012/3/14 00:00’时间段整一年的数据，组成一个新的数据框data1.

data1_1_direction = data1[(data1['CH7Avg'] > 0) & (data1['CH7Avg'] < 90)]
speed_1_x = data1_1_direction['CH3Avg']
speed_1_y = data1_1_direction['CH13Avg']
X_speed_1_x = speed_1_x[:,np.newaxis]
#2
data1_2_direction = data1[(data1['CH7Avg'] > 90) & (data1['CH7Avg'] < 180)]
speed_2_x = data1_2_direction['CH3Avg']
speed_2_y = data1_2_direction['CH13Avg']
X_speed_2_x = speed_2_x[:,np.newaxis]
#3
data1_3_direction = data1[(data1['CH7Avg'] > 180) & (data1['CH7Avg'] < 270)]
speed_3_x = data1_3_direction['CH3Avg']
speed_3_y = data1_3_direction['CH13Avg']
X_speed_3_x = speed_3_x[:,np.newaxis]

#4
data1_4_direction = data1[(data1['CH7Avg'] > 270) & (data1['CH7Avg'] < 360)]
speed_4_x = data1_4_direction['CH3Avg']
speed_4_y = data1_4_direction['CH13Avg']
X_speed_4_x = speed_4_x[:,np.newaxis]

print(data1_4_direction.head())

# 定义子函数程序	
#  定义处理数据的函数,提取不同扇区的数据,并对X进行单列行矩阵转换.
#def get_data(down,up):
	# 取数据框Data1第7通道70m风向数据进行分扇区的数据集的筛选,筛选出第n扇区的数据框.
	#导入测风数据的数据文件speedData1.csv.
	
	#data1_n_direction = data1[(data1['CH7Avg'] > down) & (data1['CH7Avg'] < up)]
    #x = data1_n_direction['CH3Avg']
    #y = data1_n_direction['CH13Avg']
   # X= x[:,newaxis]
	#return X,x,y
	
 #线性回归分析，其中X为自变量单列行矩阵。y为因变量列表。
def linear_model_fit(X,y):
	# 1. 构造回归对象
	regr = LinearRegression()
	regr.fit(X,y)
	# 2. 构造返回字典
	predictions = {}
	# 2.1 截距值
	predictions['a'] = regr.intercept_
	# 2.2 回归系数（斜率值）
	predictions['b'] = regr.coef_
	# 2.3 预测值列表
	predictions['predict_y'] = regr.predict(X)
	# 2.4 R2
	predictions['R2'] = regr.score(X,y)
	# 3 返回函数求出的结果 输入结果字典。
	return predictions

#   构造绘图函数
def show_line(x,y,p,a,b,R2,n):
	# 2. 绘出已知数据散点图
    plt.scatter(x,y,color = 'blue',s=2)
    # 3. 绘出预测直线
    plt.plot(x,p,color = 'red',linewidth = 4)
    plt.title('Revelant circle No %i'%n)
    plt.xlabel('气象站')
    plt.ylabel('测风塔70m高风速')
    plt.annotate("y=%.4f"%a+"x"+"%.4f"%b,
                xy=(9,a*9+b),
                xytext=(12,6),
                fontsize=14,
                arrowprops=dict(facecolor='black', 
                               shrink=0.05,
                               width=0.1,
                               headwidth=4,
                               headlength=9
                               )
                )
	#plt.text(X_text,Y_text-1,'R2=%.4f'%R2,fontsize=14,color='black')
    plt.show()

if __name__=='__main__':
	fig = plt.figure(figsize=(10,10))
	plt.subplot(221)
	#调用输入数据自定义函数,按风向区间取收据集,增加变换列矩阵,返回X,y
	
	#调用线性回归模型子函数,给定X单列矩阵,Y计算返回字典数据predictions:a,b,R2
	predict_1 = linear_model_fit(X_speed_1_x,speed_1_y)
	a1 = predict_1['a']
	b1 = predict_1['b']
	predict_y_1 = predict_1['predict_y'] 
	R2_1 = predict_1['R2']
	#调用绘图子函数,给定x,y数据集
	show_line(speed_1_x,speed_1_y,predict_y_1,a1,b1,R2_1,1)
	
	#subplot(222),2表示2行,2表示2列,2表示排下来的第2张图,画第2张子图.
	plt.subplot(222)
	
	#调用线性回归模型子函数,给定X单列矩阵,Y计算返回字典数据predictions:a,b,R2
	predict_2 = linear_model_fit(X_speed_2_x,speed_2_y)
	a2 = predict_2['a']
	b2 = predict_2['b']
	predict_y_2= predict_2['predict_y'] 
	R2_2 = predict_2['R2']
	#调用绘图子函数,给定x,y数据集
	show_line(speed_2_x,speed_2_y,predict_y_2,a2,b2,R2_2,2)
	
	
	
	plt.subplot(223)
	#调用线性回归模型子函数,给定X单列矩阵,Y计算返回字典数据predictions:a,b,R2
	predict_3 = linear_model_fit(X_speed_3_x,speed_3_y)
	a3 = predict_3['a']
	b3 = predict_3['b']
	predict_y_3 = predict_3['predict_y'] 
	R2_3 = predict_3['R2']
	#调用绘图子函数,给定x,y数据集
	show_line(speed_3_x,speed_3_y,predict_y_3,a3,b3,R2_3,3)
	
	plt.subplot(224)

	#调用线性回归模型子函数,给定X单列矩阵,Y计算返回字典数据predictions:a,b,R2
	predict_4 = linear_model_fit(X_speed_4_x,speed_4_y)
	a4 = predict_4['a']
	b4 = predict_4['b']
	predict_y_4 = predict_4['predict_y'] 
	R2_4 = predict_4['R2']
	#调用绘图子函数,给定x,y数据集
	show_line(speed_4_x,speed_4_y,predict_y_4,a4,b4,R2_4,4)
