# Python ChatRoom

A real-time multi-client chatroom built using Python, featuring a GUI client and a socket-based server. This project demonstrates client–server architecture, multithreading, and real-time communication, similar to a lightweight Discord-style chat.

---

## Features

- Multiple clients can connect simultaneously
- Real-time message broadcasting
- Color-coded usernames for better readability
- GUI client built with Tkinter
- Fast and lightweight socket communication
- Simple client–server architecture

---

## How It Works

- The server listens for incoming connections and handles each client in a separate thread.
- The client connects to the server and provides a graphical interface for sending and receiving messages.
- Messages are sent with a fixed-size header indicating message length to ensure reliable communication.
- The server broadcasts incoming messages to all connected clients.

---

## Project Structure
ChatRoom/
│
├── server.py # Handles connections and message broadcasting
├── client.py # GUI client (Tkinter-based)
└── README.md # Project documentation

---

## Technologies Used

- Python 3
- socket (network communication)
- threading (handling multiple clients)
- tkinter (graphical user interface)

---

## Installation and Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chatroom.git
cd chatroom
