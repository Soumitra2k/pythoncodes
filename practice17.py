###  My SQL connection with Python

import mysql.connector


conn = mysql.connector.connect(host="localhost",database="APIDevelop",user="root",password="Oracle")

cursor = conn.cursor()

print(conn.is_connected())

mysql="select * from CustomerInfo"
cursor.execute(mysql)
rows=cursor.fetchall()
print(rows)
for data in rows:
    print(data)
#print(rows)



