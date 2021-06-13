import socket
import pickle
from _thread import *
from player import Player


server = "192.168.1.103"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except Exception as e:
    str(e)

print("Waiting for connection, server started.")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected!")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print(f"Received: {data}")
                print(f"Sending: {reply}")

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection.")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to {addr}.")

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1