import socket, logging

logging.basicConfig(level=logging.INFO)

PORT = 77777

def create_socket(address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setblocking(0)  
        s.bind(address)
        s.listen(7)
        logging.info("Now listening at %s", address)
        return s
    except OSError as e:
        logging.error("Failed to create a socket: %s", e)
        raise

class hall:
    def __init__(self,name):
        self.rooms = {}
        self.room_user = {}

    def new_mb(self,user):
        user.socket.sendall(b'Please tell us your name:\n')

class Room:
    def __init__(self, name):
        self.users = [] 
        self.name =name
    
    def new_mb(self, from_user):
        msg = f"{self.name} welcomes: {from_user.name}\n"
        for user in self.users:
            user.socket.sendall(msg.encode())
    
    def broadcast(self, from_user, msg):
        full_msg = f"{from_user.name}: {msg.decode()}\n".encode()
        for user in self.users:
            user.socket.sendall(full_msg)
    
    def rm_user(self, user):
        try:
            self.users.remove(user)  
            leave_msg = f"{user.name} has left the room\n".encode()
            self.broadcast(user, leave_msg)
        except ValueError:
            print(f"User {user.name} is not in the room.")

class User:
    def __init__(self, socket, name="new"):
        self.socket = socket
        socket.setblocking(False) 
        self.name = name

    def fileno(self):
        return self.socket.fileno()

    def set_name(self, name):
        self.name = name
    
    def __str__(self):
        return f"User(name={self.name})"


class user:
    def __init__(self,socket,name):
        name = "new"
        self.socket = socket
        socket.setblocking(0)
        self.name = name

    def fileno(self):
        return self.socket.fileno()

