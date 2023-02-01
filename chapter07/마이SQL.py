import pymysql

con = pymysql.connect(host = 'localhost', user='root', password='12345', db='test', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()

sql = "SELECT * FROM admin"
cur.execute(sql)
rows = cur.fetchall()
con.close() #db 연결 종료
print(type((rows)))
print(rows)
