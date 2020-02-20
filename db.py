import mysql.connector as mc

#connect to server
db = mc.connect(user="localhost", user="root", passwd="toor")

#create cursor
c = db.cursor()

#create database
c.execute("CREATE DATABASE IF NOT EXISTS EMPLOYEE")

#CONNECT OT DATABASE
db = mc.connect(user="localhost", user="root", passwd="toor", database="EMPLOYEE")

#CREATE TABLE 
sql = """CREATE TABLE EMPLOYEE(
 FIRST_NAME CHAR(20) NOT NULL,
 LAST_NAME CHAR(20),
 AGE INT,
 SEX CHAR(1),
 INCOME FLOAT)"""

c.execute(sql)

#disconnect from server
db.close()