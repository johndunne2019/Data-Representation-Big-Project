import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="stockbullfinder"
)

mycursor = mydb.cursor()
sql="CREATE TABLE bulls (id INT AUTO_INCREMENT PRIMARY KEY, code VARCHAR(10), name VARCHAR(250), breed VARCHAR(3), owner VARCHAR(250))"

mycursor.execute(sql)