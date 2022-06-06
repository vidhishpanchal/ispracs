# Required Pycryptodome to function
from base64 import encode
import socket
from Crypto.Hash import SHA256
socket = socket.socket()
port = 4321
socket.bind(('', port))
socket.listen(5)
print("Server has successfully started !")
try:
for i in range(0,10):
conn, addr = socket.accept()
print('Got connection from %s:%s'%(addr[0],addr[1]))
print("-------------------SERVER-------------------\n")
print("-------------RSA IMPLEMENTATION-------------")
p1 = 89
p2 = 83
nr = p1*p2
phi = (p1-1)*(p2-1)
print(f"Two prime numbers are : {p1} and {p2}")
print(f"Euler's totient function (z) = {phi}")
e = 5
d = 5773
print("Calculated value of e = 5 and d = 5773")
print("--------------------------------------------\n")
hash = SHA256.new()
print("Initialized public and private keys and the required hashing
algorithms.")
ks1, ns = list(map(int,conn.recv(1024).decode().split('::')))
print("Received ks1::ns from sender.")
conn.send((str(e)+"::"+str(nr)).encode())
print("Sent message e::nr to sender.")
s, c1 = conn.recv(4096).decode().split('::')
print("Received message s::c1 from sender.")
s_deciphered = "".join([chr(pow(int(i),ks1)%ns) for i in s.split('
')])
m1 = "".join([chr(pow(int(i),d)%nr) for i in c1.split(' ')])
hash.update(m1.encode('utf-8'))
d1 = hash.hexdigest()
if(d1 == s_deciphered):
conn.send("Verification successful !".encode())
print("Verification successful !")
print("Message is:", m1)
else:
conn.send("Invalid!".encode())
print("Invalid!")
conn.close()
socket.close()
except:
socket.close()
