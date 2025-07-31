import socket

HOST = '0.0.0.0'
PORT = 2323

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Telnet server running on port {PORT}")
    while True:
        conn, addr = s.accept()
        print(f"[!] Connection from {addr}")
        conn.sendall(b"Welcome to IoT Device (Simulated Telnet)\n")
        conn.sendall(b"No login required! You are now root.\n$ ")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b"Command received: " + data + b"$ ")
        conn.close()
