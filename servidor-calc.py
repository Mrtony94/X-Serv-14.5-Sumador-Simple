#!/usr/bin/python3

import socket
import calculadora


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        text = str(recvSocket.recv(2048), 'utf-8')
        print(text)
        info = text.split(' ')[1]
        if len(info.split('/')) == 4:
            num1 = float(info.split("/")[1])
            operacion = info.split("/")[2]
            num2 = float(info.split("/")[3])
            try:
                resultado = calculadora.Function_P[operacion](num1, num2)
                resultado = str(resultado)
                resultado = bytes(resultado, 'utf-8')
                recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                b"<html><body><h1>El resultado es: " + resultado + b"</h1></body></html>" +
                b"\r\n")
                recvSocket.close()
            except ZeroDivisionError:
                recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n<html><body><h1>No dividas entre 0.</h1></body></html>\r\n")
                recvSocket.close()

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
