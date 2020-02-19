import time
import pandas as pd
import sqlite3
from contextlib import contextmanager

table1 = {'names': ["doritos", "simba"],
          'col': "p_name TEXT, c_price REAL, s_price REAL, amt_b INT, amt_s INT",
          'col_c': "p_name, c_price, s_price, amt_b, amt_s",
          'cp': [3, 3],
          'sp': [6,6],
          'amt_b':[100, 100],
          'amt_s': [55,65]
          }
        
_st = table1["col"]
_values = []



conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.execute('CREATE TABLE chips (p_name TEXT, c_price REAL, s_price REAL, amt_b INT, amt_s INT)')

for j,pname in enumerate(table1["names"]):
    c.execute("INSERT INTO chips VALUES (?, ?, ?, ?, ?)", (pname, table1["cp"][j], table1["sp"][j], table1["amt_b"][j], table1["amt_s"][j],))

c.execute("SELECT s_price * amt_s-c_price*amt_b FROM chips WHERE p_name=='doritos'")
doritos_profit = c.fetchone()

c.execute("SELECT s_price * amt_s-c_price*amt_b FROM chips WHERE p_name=='simba'")
simba_profit = c.fetchone()

print("profit of doritos: {}\nProfit of simba: {}".format(doritos_profit, simba_profit))
c.execute("ALTER TABLE chips ADD profit REAL")
conn.commit()
c.execute('SELECT c_price, s_price, amt_b, amt_s FROM chips')

d = {"simba":[]}
rows = c.fetchall()
for row in rows:
    print(rows)    
cost = 0.0
selling = 0.0
amount_bought = 0
amount_sold = 0
profit = 0
row_first = rows[0]

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

drow = c.fetchall()
d["simba"] = drow[0]
d["lays"] = drow[1]
df = pd.DataFrame(d, columns=["simba", "lays"])
df = df.drop([0])
print(df)

for r in c.fetchall():
    time.sleep(2)
    print("\nprinting table...")
    time.sleep(2)
    print("\n\n|product Name | cost price | selling price | quantity bought | quantity sold | profit |\n\n|{} | {} | {} | {} | {} | {} |".format(r[0], r[1], r[2], r[3], r[4], r[5]))


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
