# Open command prompt in admin mode
# python -m pip install mysql-connector-python
# If you get pip upgradation message then run this command first
# python -m pip install --upgrade pip
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)