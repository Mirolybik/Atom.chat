import hashlib as hash
import sqlite3 as sq
import socket,random,datetime,getpass
from threading import Thread
from colorama import Fore, init, Back

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

print("1. Registrate")
print("2. Login")
nok=int(input("Gouse: "))

def user_check(name,passwd):
    data_users= name , passwd
    read_db = "SELECT * FROM users"
    cursor.execute(read_db)
    data= cursor.fetchall()
    if data_users in data:
        return True
    else:
        return False


if nok == 1:
    name = input("Enter your name: ")
    passwd = getpass("Enter your password: ")
    password_hash = hash.sha256(passwd.encode("utf-8")).hexdigest()
    if user_check(name,password_hash):
        print("user is login")
        exit()
    else:
        data_users= name , password_hash
        reqtidb = '''INSERT INTO users (login,password) VALUES (?,?)'''
        cursor.execute(reqtidb,data_users)
        db.commit()
        print("Connect")

elif nok == 2:
    name = input("Enter your name: ")
    passwd = getpass("Enter your password: ")
    password_hash = hash.sha256(passwd.encode("utf-8")).hexdigest()

    if user_check(name,password_hash):
        print ("Connect")
    else:
        print("user is un login")
        exit()

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
