import mysql.connector as mc

#db = mc.connect(host="localhost", user="root", passwd="toor")
#c = db.cursor()
#c.execute("CREATE DATABASE IF NOT EXISTS employee")

db = mc.connect(host="localhost", user="root", passwd="toor", database="employee")
c = db.cursor()
#c.execute("""CREATE TABLe employee(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)""")
c.execute("""INSERT INTO employee(FIRST_NAME,LAST_NAME, AGE,SEX,INCOME) VALUES (%s,%s,%s,%s,%s)""" , ('Mac', 'Mohan', 20, 'M', 2000))
db.commit()
c.execute("UPDATE employee SET AGE = (AGE + 1) WHERE SEX='%c'" % ('M'))
db.commit()
c.execute("SELECT * FROM employee WHERE INCOME > %d"%(1000))
results = c.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]

print(f"fname={fname}\n lname={lname}\n age={age}\n sex={sex}\n income={income}")
c.execute("DELETE FROM employee WHERE AGE > '%d'" % (19))
c.execute("SELECT * FROM employee")

print(c.fetchone())
db.close()