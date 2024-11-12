import sqlite3 as sq
import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
from getpass import getpass

init()

db= sq.connect("users.db")
cursor = db.cursor()
users_db = '''
    CREATE TABLE IF NOT EXISTS users (
            login TEXT PRIMARY KEY,
            password TEXT NOT NULL
            );
'''

cursor.execute(users_db)
db.commit()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = random.choice(colors)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 
separator_token = "<SEP>" 

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
name = input("Enter your name: ")
passwd = getpass("Enter password: ")

data_users= name , passwd
read_db = "SELECT * FROM users"
cursor.execute(read_db)
data= cursor.fetchall()

if data_users in data:
    print("user is online")
else:
    print("user in offline")
    reqtidb = '''INSERT INTO users (login,password) VALUES (?,?)'''
    cursor.execute(reqtidb,data_users)
    db.commit()

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())

s.close()
