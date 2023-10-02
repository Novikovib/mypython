import socket

HOST = "127.0.0.1"
PORT = 9000


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Bla bla bla")
        #data = s.recv(20)
        #print(f"Received {data}")
