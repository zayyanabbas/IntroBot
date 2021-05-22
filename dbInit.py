import sqlite3

connection = sqlite3.connect('introductions.db')
print("DB OPENED")


connection.execute('''CREATE TABLE INTROS
         (ID           TEXT PRIMARY KEY  NOT NULL,
          INTRODUCTION TEXT              NOT NULL);''')

print('DB CREATED')

#cursor = connection.execute("SELECT introduction from INTROS where id='aa'")
#no = connection.execute("SELECT id, introduction from INTROS")

#for row in no:
#    print('y')
#    print(row[0], row[1])

connection.close()