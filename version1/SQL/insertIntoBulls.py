  
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="stockbullfinder"
)

cursor = db.cursor()
sql="insert into bulls (code, name, breed, owner) values (%s,%s,%s,%s)"
values = ("FSZ", "Fiston", "CH", "National Cattle Breeding Center")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)