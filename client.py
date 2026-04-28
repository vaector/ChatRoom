import socket
import threading
import random
from tkinter import *

HEADER = 64
FORMAT = "utf-8"
PORT = 12345
SERVER = "127.0.0.1"   # safer than gethostbyname
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user_colors = {}
colors = ["red", "green", "blue", "magenta", "cyan", "orange"]

# Init WINDOW
root = Tk()
root.title("Chat Client")
root.geometry("600x500")
root.configure(bg="black")

Label(root, text="Enter your name:", bg="red", fg="white").pack(pady=5)
name_entry = Entry(root)
name_entry.pack(pady=5)

chat_frame = Frame(root, bg="black")
chat_frame.pack(fill=BOTH, expand=True)

msg_entry = Entry(root)
msg_entry.pack(fill=X, padx=10, pady=5)

def connect():
    try:
        client.connect(ADDR)
        threading.Thread(target=receive, daemon=True).start()
        print("Connected to server.")
    except Exception as e:
        print("Connection failed:", e)

def receive():
    while True:
        try:
            header = client.recv(HEADER).decode(FORMAT)
            if not header:
                break

            msg_length = int(header.strip())
            msg = client.recv(msg_length).decode(FORMAT)

            if ":" in msg:
                sender, text = msg.split(":", 1)
                sender = sender.strip()

                if sender not in user_colors:
                    user_colors[sender] = random.choice(colors)

                color = user_colors[sender]

                Label(chat_frame, text=f"{sender}:{text}", bg="black", fg=color)\
                    .pack(anchor="w", padx=10, pady=2)
            else:
                Label(chat_frame, text=msg, bg="black", fg="white")\
                    .pack(anchor="w", padx=10, pady=2)

        except:
            break

def send_message(event=None):
    name = name_entry.get().strip()
    msg = msg_entry.get().strip()

    if not name or not msg:
        return

    full_msg = f"{name}: {msg}"
    data = full_msg.encode(FORMAT)

    msg_length = str(len(data)).encode(FORMAT)
    msg_length += b' ' * (HEADER - len(msg_length))

    client.sendall(msg_length)
    client.sendall(data)

    msg_entry.delete(0, END)

Button(root, text="Connect", command=connect).pack(pady=5)
Button(root, text="Send", command=send_message).pack(pady=5)

msg_entry.bind("<Return>", send_message)

root.mainloop()