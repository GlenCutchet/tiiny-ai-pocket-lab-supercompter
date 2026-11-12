import socket

TIINY_IP = "172.28.167.161"
PORT = 80  # Replace with the target port your Tiiny app is listening on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((TIINY_IP, PORT))
        s.sendall(b"Hello from Win11 Python client!")
        data = s.recv(1024)
        print("Received from Tiiny:", data.decode())
    except socket.error as e:
        print("Socket connection failed:", e)