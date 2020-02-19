import sqlite3
from contextlib import contextmanager

table1 = {'names': ["doritos", "simba"],
          'col': "p_name TEXT, c_price REAL, s_price REAL, amt_b INT, amt_s INT",
          'col_c': "p_name, c_price, s_price, amt_b, amt_s",
          'cp': [3, 3],
          'sp': [6,6],
          'amt_b':[100, 200],
          'amt_s': [50,65]
          }
        
_st = table1["col"]
_values = []

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('CREATE TABLE chips (p_name TEXT, c_price REAL, s_price REAL, amt_b INT, amt_s INT)')

c.execute("INSERT INTO chips VALUES ('doritos', 3, 6, 2200, 580)")

f = c.execute("SELECT c_price FROM chips WHERE p_name=='doritos'")
c.execute("ALTER TABLE chips ADD profit REAL")

conn.commit()


c.execute('SELECT c_price, s_price, amt_b, amt_s FROM chips')


rows = c.fetchall()

print(rows)

cost = 0.0
selling = 0.0
amount_bought = 0
amount_sold = 0
profit = 0
row_first = rows[0]
print(row_first)

cost = row_first[0]
selling = row_first[1]
amount_bought = row_first[2]
amount_sold = row_first[3]
print(cost, selling,amount_bought, amount_sold)
Profit = (selling*amount_sold)-(cost*amount_bought)
print(Profit) 

c.execute("UPDATE chips SET profit=?", (Profit,) )    
conn.commit()
c.execute("SELECT * FROM chips")
print(c.fetchall())


"""
@contextmanager
def create_table(cursor, tname, columns): 
    cursor.
    c.execute(f'')
    try:
        yield
    finally:
        cursor.execute(f'SELECT * FROM {tname}')
        cursor.fetchall()



def update_table(cursor, col, value, check, value2):
    cursor.execute(f'UPDATE {col} SET {col} = "{value}" WHERE {check}="{value2}"')
    
        
with conn:
    
    for n in table1["names"]:
        with create_table(c, n, table1["col"]):
            update_table(c, "amt_b", "110", "s_price", "6" )
                       
"""
