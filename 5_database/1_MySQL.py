import pymysql
from pymysql.cursors import DictCursor

db = pymysql.Connect(
    host='localhost',
    port=3306,
    db='spider',
    user='root',
    password='20020224.',
    charset='utf8',
    autocommit=True
)

cursor = db.cursor(cursor=DictCursor)
sql = 'select * from lianjia where id<%s;'
row = cursor.execute(sql, 100)
print(row)
print(cursor.fetchall())





