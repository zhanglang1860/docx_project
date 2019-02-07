
# -*- coding:utf-8 -*-  
# 设置中文utf-8解释环境标识
# No例1:气象站长期年平均风速的条形图绘制方法示例及代码详解

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd  #导入pandas包
import pylab as pl
import numpy as np

mpl.rcParams["font.sans-serif"]=["SimHei"] # 设置坐标轴标识字符串中的中文标识的字体为黑体
mpl.rcParams['axes.unicode_minus'] = False # 不使用默认的unicode minus模式来处理坐标轴轴线的刻度标签为负数的情况。
                      
data = pd.read_csv("no1_anex_bar.csv") #pandas 中输入EXCEL表格数据CSV的方法
print(data)#测试数据输入是否成功
print("===================================")

print(data["year"])#测试数据框的以头标识为year的一维向量的数值调用方法
print("===================================")
Xyear=data["year"] #将年数值向量附值给Xyear

Yspeed=data["speed"] #将风速向量附值给Yspeed

plt.figure(figsize=(9, 6)) #创建figure窗口画布大小
pl.xticks(rotation=45) #设置条形图X轴的刻度标签的旋转方向
# 绘制BAR图
plt.bar(Xyear,Yspeed,align="center",color="lightsteelblue",tick_label=Xyear,hatch="",alpha=0.9,width=0.4,label="气象站年平均风速A")
# 条形图的各参数请参加bar 参数设置手册

#绘制气象站风速平均值水平参考线
avg=np.mean(Yspeed)
plt.axhline(y=avg,C="r",ls="--",lw=2)
#绘制图纸区域的指向性文本描述，如：多年平均风速值
x1=2003.5
y1=avg+0.05
plt.text(x1,y1,"多年平均风速值",weight="bold",color="black",fontsize=12)
#设置XY坐标轴的中文标签
plt.xlabel("年份",fontsize=12)
plt.ylabel("风速",fontsize=12)


#设置Y轴在网格线
plt.grid(True,axis="y",ls=":",color="green",alpha=0.3) #注意这里"y"指Y坐标轴，不能采用变量Yspeed写入。
#设置Y轴的坐标取值范围
plt.ylim(1,3) #Y轴起点1,终点3.
#设置图例标签
plt.title("气象站多年年平均风速分布图")

# 关于人工站与自动站数据的叠加分析,图形叠加分析
data1 = pd.read_csv("no1_anex_bar2.csv") #pandas 中输入EXCEL表格后10年自动站数据CSV的方法
Xyear1=data1["year"] #将年数值向量附值给Xyear1
Yspeed1=data1["speed"] #将风速向量附值给Yspeed1
width=0.4  #设定后10年柱状图与原来柱状图在X的位置偏移量
plt.bar(Xyear1+width,Yspeed1,width,align="center",color="#FFA500",hatch="",alpha=0.9,label="气象站年平均风速B")

# 设置X轴的不同情况的刻度位置及刻度标签

#plt.xticks([index+(width/2) for index in Xyear],Xyear)
	
plt.legend() #设定不同线条的标签标识
#显示图形
plt.show()
