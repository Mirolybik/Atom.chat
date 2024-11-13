import sqlite3 as sq

connection = sq.connect('test.db')
cursor = connection.cursor()

products_tb = '''
CREATE TABLE IF NOT EXISTS products (
     login TEXT PRIMARY KEY,
     password TEXT NOT NULL);
'''

cursor.execute(products_tb)
connection.commit()

new_product = ('ivan','ivanino')

request_to_insert_data = '''
INSERT INTO products (login,password) VALUES (?, ?);
'''

cursor.execute(request_to_insert_data, new_product)
connection.commit()

