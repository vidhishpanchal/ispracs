import socket
from Crypto.Hash import SHA256
socket = socket.socket()
port = 4321
socket.connect(('127.0.0.1', port))
print("-------------------CLIENT-------------------\n")
print("-------------RSA IMPLEMENTATION-------------")
p1 = 79
p2 = 73
phi = (p1-1)*(p2-1)
ns = p1*p2
print(f"Two prime numbers are : {p1} and {p2}")
print(f"Euler's totient function (z) = {phi}")
e = 5
d = 4493
print("Calculated value of e = 5 and d = 5773")
print("--------------------------------------------\n")
hash = SHA256.new()
print("Initialized public and private keys and the required hashing
algorithms.")
socket.send((str(e)+"::"+str(ns)).encode())
print("Sent the message e::ns to receiver.")
kr1, nr = list(map(int,socket.recv(1024).decode().split("::")))
print("Received the message kr1::nr from receiver.")
m1 = input("Enter the message: ")
hash.update(m1.encode())
d1 = hash.hexdigest()
c1 = " ".join([str(pow(ord(i),kr1)%nr) for i in m1])
s = " ".join([str(pow(ord(i),d)%ns) for i in d1])
socket.send((s+"::"+c1).encode())
print("Sent the message s::c1 to receiver.")
print(socket.recv(1024).decode())
socket.close()