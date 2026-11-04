# 5a_Create_Socket_for_HTTP_for_webpage_upload_and_download

## NAME
T.Goshanrajan

## REGISTER NUMBER

212225040098

## AIM

To write a Python program using socket programming to perform HTTP file upload and download between a client and a server.

## SOFTWARE REQUIREMENTS

* Python 3.x
* Visual Studio Code / IDLE
* Command Prompt / Terminal

## ALGORITHM

1. Start the program.
2. Create a socket connection between the client and server.
3. Start the server and wait for client requests.
4. Get the filename from the client.
5. Send an HTTP POST request to upload the file.
6. The server receives and stores the uploaded file.
7. The server sends an ACK response if the upload is successful; otherwise, it sends an error response.
8. Send an HTTP GET request to download the file.
9. The server sends the requested file to the client.
10. Save the downloaded file on the client side.
11. Stop the program.

## PROGRAM

### 1. SERVER PROGRAM (server.py)

```python
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
```

### 2. CLIENT PROGRAM (client.py)

```python
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
```

## EXECUTION PROCEDURE

1. Create a folder named `HTTP_File_Transfer`.
2. Create two Python files named `server.py` and `client.py`.
3. Create a text file named `example.txt` containing sample text.
4. Open the terminal and start the server:

```bash
python server.py
```

5. Open another terminal and execute the client:

```bash

python client.py
```

6. The client uploads `example.txt` to the server.
7. The server stores the uploaded file as `uploaded.txt`.
8. The client sends a download request.
9. The server transfers the file back to the client as `downloaded.txt`.
10. Verify the contents of the downloaded file.

## OUTPUT

<img width="1293" height="215" alt="Screenshot 2026-11-04 143642" src="https://github.com/user-attachments/assets/f6fa29c9-698f-4f30-81e9-1b483d3c4533" />
<img width="1305" height="283" alt="Screenshot 2026-11-04 143710" src="https://github.com/user-attachments/assets/36ab269c-0569-42d4-adce-6447e686f6b0" />


**Generated Files:**

* example.txt – Original file
* uploaded.txt – File stored on the server
* downloaded.txt – Downloaded file received from the server

## RESULT

Thus, the Python socket programming application for HTTP file upload and download was successfully created and executed. The client successfully uploaded a file to the server and downloaded the file using HTTP GET and POST requests.

