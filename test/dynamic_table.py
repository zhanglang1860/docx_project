from docxtpl import DocxTemplate
# coding=utf=8
import pymysql
import numpy as np

db = pymysql.connect(host='localhost', user='root', passwd='Yuwen520', port=3306, db='tur', charset='utf8')
cur = db.cursor()
sql_str = ''
data_name = ('GW3.3-155', 'MY2.5-145', 'MY3.2-145', 'GW140-3.4', 'En2.5-141')
# data_name = ('GW3.3-155', 'MY2.5-145', 'MY3.2-145', 'GW140-3.4', 'En2.5-141', 'GW3.0-140', 'En3.0-141')

for i in range(len(data_name)):
    if i == len(data_name) - 1:
        sql_str = "("+sql_str + '\'%s\')'
    else:
        sql_str = sql_str + '\'%s\','
print(sql_str)

# selectsql = "SELECT * FROM tur_model WHERE tur_type_name in " + "('%s','%s','%s','%s','%s','%s','%s')"
selectsql = "SELECT * FROM tur_model WHERE tur_type_name in " + sql_str

cur.execute(selectsql % data_name)
data = cur.fetchall()  # 所有
# for item in data:
#     print(item)
db.close()
data_np = np.array(data)

#
tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\untitled\files\华润template.docx')

context = {}
for i in range(0, 16):
    if i < 13:
        key = 'tbl_contents' + str(i)
        value = data_np[:, i + 1]
        context[key] = value
    else:
        key = 'tbl_contents' + str(i)
        value = data_np[:, i + 4]
        context[key] = value
print(context)

tpl.render(context)
tpl.save(r'C:\Users\Administrator\PycharmProjects\untitled\files\result.docx')
