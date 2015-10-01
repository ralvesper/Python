import mysql.connector

conn = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='PORTAL_MOBILE')

cursor = conn.cursor()
cursor.execute("SELECT * FROM PM_USUARIO")
 
row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

conn.close()