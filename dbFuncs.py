from itertools import chain
import sqlite3
connection = sqlite3.connect('introductions.db')

#connection.execute("INSERT INTO INTROS (ID,INTRODUCTION) VALUES ('A', 'BOBBY')")

#connection.close()

cursor = connection.execute("SELECT introduction from INTROS where id='aa'")
#no = connection.execute("SELECT id, introduction from INTROS")

#for row in no:
#    print('y')
#    print(row[0], row[1])
print(cursor)

try:
    first_row = next(cursor)
except StopIteration as e:
    print('a')
    pass

connection.close()