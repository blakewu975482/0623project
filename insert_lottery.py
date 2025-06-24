import mysql.connector

print("建立資料庫連線中")
cnx=mysql.connector.connect(
    host="localhost",
    port= 3306,
    user="ru",
    password="1234",
    database="prize"
)

print("透過連線取得cursor物件")
dbcursor=cnx.cursor()
print("執行 insert")
insertSQL="insert into lottery(n1,n2,n3,n4,n5,n6) values(%s,%s,%s,%s,%s,%s)"

parserdata=(4,18,21,23,37,42)

dbcursor.execute(insertSQL,parserdata)
print("完成交易 確定要寫入資料庫")
cnx.commit()

dbcursor.close()
cnx.close()