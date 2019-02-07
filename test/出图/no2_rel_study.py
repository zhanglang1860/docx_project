
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

#导入测风数据的数据文件speedData1.csv.
data = pd.read_csv("speedData1.csv") #pandas 中输入EXCEL表格分隔数据CSV格式的方法

data['Date']= pd.to_datetime(data['Date'],format='%Y/%m/%d %H:%M') 
#设定数据框中的Date时间列表的数据为时间数据格式(包括 Y m d H M S)。
data = data.set_index('Date') # 设定数据的时间序列索引'Date'
data1 = data['2011/3/13 00:00':'2012/3/14 00:00']
#根据时间序列的索引格式，调取‘2011/3/13 00:00’至‘2012/3/14 00:00’时间段整一年的数据，组成一个新的数据框data1.

speed_50m=data1["CH3Avg"] #取数据框中CH3AVg通道50m高度风速列向量数据
speed_70m=data1["CH13Avg"] #取数据框中CH13AVg通道70m高度风速列向量数据

# 画散点图，寻找变量与变量之间的关系
fig = plt.figure(figsize=(8,5))
plt.scatter(speed_50m,speed_70m,marker='o',s=5) 
plt.xlabel('50m高10mim平均风速',size=12)
plt.ylabel('70m高10mim平均风速',size=12)
plt.title('同一测风塔不同测层之间的相关性检验',size=12)

# 分析相关性直线的绘制与相关系数R平方‘R2’显著性检验
import math
import scipy 
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score
# 创建线性模型
regr = linear_model.LinearRegression()

# 我们需要将列表数据speed_50m调整为[n_samples, n_features]的特征矩阵，得到矩阵X_speed_50m
# 增加一个空数据行,或数据全为1的行,转换列表为线性方程组的X系数矩阵.见 sklearn-linear_model.LinearRegression 官方实例解释.
# 也可以采用X_speed_50m = speed_50m.array.reshape(-1,1)进行转换矩阵.
X_speed_50m = speed_50m[:,np.newaxis] 

# 将线性方程的特征矩阵X_speed_50m与一维列表speed_70m进行模型的一元回归线性模拟。
regr.fit(X_speed_50m,speed_70m)

# 将线性方程的系数矩阵X_speed_50m带入预测函数求取预测值一维数组列表predict_70m.
predict_70m=regr.predict(X_speed_50m)

# 求取模拟后的直线方程的截距b,和方程的相关系数a. 即b=regr.intercept_,a=regr.coef_
b=regr.intercept_
a=regr.coef_
R2=regr.score(X_speed_50m,speed_70m)
print(X_speed_50m)
print(speed_70m)
print(speed_50m.shape)
print("b=%f"%b)
print("a=%.2f"%a)
print("R2=%.2f"%R2)
if R2>0.7:
	print("显著性分析结论：")
	print("-" *20)
	print("线性回归模型显著,两测风塔的不同测层相关性显著")
else:
	print("显著性分析结论：")
	print("-" *20)
	print("线性回归模型不显著,两测风塔的不同测层相关性不显著")


plt.plot(speed_50m,predict_70m,color = 'black',linewidth = 1)   
X_arrow_text=9
Y_arrow_text=a*9+b
X_text=X_arrow_text+3
Y_text=Y_arrow_text-3

plt.annotate("y=%.4f"%a+"x"+"%.4f"%b,
             xy=(X_arrow_text,Y_arrow_text),
             xytext=(X_text,Y_text),
             fontsize=14,
             arrowprops=dict(facecolor='black', 
                             shrink=0.05,
                             width=0.1,
                             headwidth=4,
                             headlength=9
                             )
             )
plt.text(X_text,Y_text-1,'R2=%.4f'%R2,fontsize=14,color='black')
#如果采用text,就没有箭头与指引线,方法为plt.text(15,7,"y=%.4f"%a+"x"+"%.4f"%b)

plt.show()



