import sqlite3 as sq

db = sq.connect('users.db')
cursor = db.cursor()

users_db = '''
CREATE TABLE IF NOT EXISTS users (
        login TEXT PRIMARY KEY,
        password TEXT NOT NULL);
'''

cursor.execute(users_db)
db.commit()

name=input()
passwd=input()

new_user=name,passwd

read_db = "SELECT * FROM users"
cursor.execute(read_db)

data = cursor.fetchall()

for row in data:
    if (name and passwd) in  data:
        print("false")
    elif (name and passwd) not in data:


request= '''
INSERT INTO products (login,password) VALUES (?, ?);
'''



cursor.execute(request,new_user)
db.commit()

