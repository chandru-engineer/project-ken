import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="2xCQTgSOEc",
  password="6ZKVa91Jga",
  database="2xCQTgSOEc"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM app_ordermodel")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
