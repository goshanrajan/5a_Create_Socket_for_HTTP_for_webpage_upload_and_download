import socket

server = socket.socket()
server.bind(('localhost', 8080))
server.listen(5)

print("HTTP Server started...")

while True:
    conn, addr = server.accept()
    request = conn.recv(4096)

    if b"POST /upload" in request:
        header, data = request.split(b'\r\n\r\n', 1)

        with open("uploaded.txt", "wb") as f:
            f.write(data)

        response = b"HTTP/1.1 200 OK\r\n\r\nFile Uploaded Successfully"

    elif b"GET /download" in request:
        try:
            with open("uploaded.txt", "rb") as f:
                data = f.read()

            response = (
                b"HTTP/1.1 200 OK\r\n"
                + b"Content-Length: " + str(len(data)).encode()
                + b"\r\n\r\n" + data
            )

        except FileNotFoundError:
            response = b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"

    else:
        response = b"HTTP/1.1 400 Bad Request\r\n\r\nInvalid Request"

    conn.sendall(response)
    conn.close()