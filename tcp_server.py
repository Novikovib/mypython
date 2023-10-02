import socket
import sys

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 9000))
        s.listen(1)
        conn, addr = s.accept()

        with conn:
            print(f"Connection accepted from {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
except Exception as e:
    print(f"Exception: {e}")
    sys.exit()
