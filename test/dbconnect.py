# coding=utf=8
import pymysql
db = pymysql.connect(host='localhost', user='root', passwd='Yuwen520', port=3306, db='tur', charset='utf8')
cur = db.cursor()
# cur.execute('localhost_3306')
selectsql = "SELECT * FROM tur_model WHERE tur_type_name in "+"('%s','%s')"
data = ('GW3.3-155','MY2.5-145',)
cur.execute(selectsql % data)
data = cur.fetchall() #所有
for item in data:
    print(item)
db.close()

print(data[0][1])

