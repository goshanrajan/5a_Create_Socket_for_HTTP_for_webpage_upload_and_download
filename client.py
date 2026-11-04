import socket

def send_request(request):
    s = socket.socket()
    s.connect(('localhost', 8080))
    s.sendall(request)
    
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

    s.close()
    return response

# Upload file
with open("example.txt", "rb") as f:
    content = f.read()

request = (
    b"POST /upload HTTP/1.1\r\n"
    b"Host: localhost\r\n"
    b"Content-Length: " + str(len(content)).encode()
    + b"\r\n\r\n" + content
)

response = send_request(request)
print("Upload Response:", response.decode())

# Download file
request = b"GET /download HTTP/1.1\r\nHost: localhost\r\n\r\n"

response = send_request(request)
header, content = response.split(b'\r\n\r\n', 1)

with open("downloaded.txt", "wb") as f:
    f.write(content)

print("File Downloaded Successfully!")