import mysql.connector

dataBase = mysql.connector.connect(

     host = "localhost",
     user = "root",
     passwd = "Manu240586@3"
	)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")

print("ALL done!")