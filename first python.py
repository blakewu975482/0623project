import mysql.connector

print("建立資料庫連線中")
cnx=mysql.connector.connect(
    host="localhost",
    port= 3306,
    user="ru",
    password="1234",
    database="world"
)

print("透過連線取得cursor物件")
dbcursor=cnx.cursor()
print("執行 select name from city")
print("記得開權限")

dbcursor.execute("select name from city")
for cityname in dbcursor:
    print(cityname)