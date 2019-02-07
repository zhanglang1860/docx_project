# -*- coding: UTF-8 -*- 
#!/usr/bin/env python
import re
import glob
listglob = []
listglob = glob.glob(r'H:\百度云下载\气站数据\30年基准气象站风资源数据\基准气象站风资源数据\风向风速\*.txt')
listglob.sort()


from PIL import Image
for filepath in listglob:
    f1 = open(filepath,'r')
    f2 = open(r'H:\百度云下载\气站数据\30年基准气象站风资源数据\基准气象站风资源数据\car_val1.txt','a')
    for line in f1.readlines():
            if re.findall('59265',line): #查找“空格1”的行 每行的格式000005 -1\n 000007  1
                f2.write(line) #把查找到的行写入f2.
    f1.close()
f2.close()

