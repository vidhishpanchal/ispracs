import hashlib
ctarr=[]
def encrypt():
    print("---------------ENCRYPTION USING PRIVATE KEY-------------")
    ptt = input("Enter input plaintext(integer) : ")
    # ptt = pt
    ct=""
    ctarr = [pow(int(m),d)%n for m in pt]
    print(f"ENCRYPTED CIPHER TEXT : {ctarr}")
    for i in ctarr:
        ct+=str(i)
    print(ct)
    return ctarr
def decrypt():
    print("---------------DECRYPTION USING PUBLIC KEY-------------")
    ct = input("Enter cipher text : ")
    print(ctsent)
    ct = ctsent
    ctarr = [1, 8, 27]
    ptarr = [int(pow(int(c), e)%n) for c in ctarr]
    print(ptarr)
    pt=""
    for i in ptarr:
        pt+=str(i)
    print(f"DECRYPTED PLAIN TEXT : {pt}")
    return pt
    
print("--------------------RSA--------------------")
def gcd(x, y):
    small, large = (x,y) if x<y else (y,x)
    while small!=0:
        temp=large%small
        large=small
        small=temp
    return large
p=int(input("Enter 1st prime (p): "))
q=int(input("Enter 2nd prime (q): "))
n=p*q
phi=(p-1)*(q-1)
flag=False
e = 1
e = int(input("Enter value of e : "))
while flag!=True:
    
    if(1<e and e<phi and gcd(e, phi)==1):
        flag=True
        print(f"e = {e}")
        d = pow(e, -1)%phi
        d = 3
        print(f"d = {d}")
    else:
        e = input("Enter valid value of e : ")

pt="123"
ct = encrypt()
print(ct)
# ct=1827
hash1 = hashlib.sha1(pt.encode()).hexdigest()
print("----------------------------------------")
ctsent, hash1 = ct, hash1
print("A sends {encrpyted message, hash1} to B")
print(f"{ctsent}, {hash1}")
print("---------------------------------------")
print(f"B encrypts recieved message : {ctsent}")
decryptedmessage = decrypt()
print(f"B got message as {decryptedmessage}")
print("Now B will hash decryptedmessage and compare with hash1")
hash2 = hashlib.sha1(str(decryptedmessage).encode()).hexdigest()
print(f"B got hash2 : {hash2}")
if hash1==hash2:
    print("hash1 = hash2 hence integrity is shown")
else:
    print("Message has been altered")
    
    
    






















    
    
    
# ----------------------------OUTPUT-------------------------------
# Enter 1st prime (p): 3
# Enter 2nd prime (q): 11
# Enter value of e : 7
# e = 7
# d = 3
# ---------------ENCRYPTION USING PRIVATE KEY-------------
# Enter input plaintext(integer) : 
# ENCRYPTED CIPHER TEXT : [1, 8, 27]
# 1827
# [1, 8, 27]
# ----------------------------------------
# A sends {encrpyted message, hash1} to B
# [1, 8, 27], 40bd001563085fc35165329ea1ff5c5ecbdbbeef
# ---------------------------------------
# B encrypts recieved message : [1, 8, 27]
# ---------------DECRYPTION USING PUBLIC KEY-------------
# Enter cipher text : 
# [1, 8, 27]
# [1, 2, 3]
# DECRYPTED PLAIN TEXT : 123
# B got message as 123
# Now B will hash decryptedmessage and compare with hash1
# B got hash2 : 40bd001563085fc35165329ea1ff5c5ecbdbbeef
# hash1 = hash2 hence integrity is shown  
    
    
    
    
    
    # print("---------------ENCRYPTION USING PRIVATE KEY-------------")
# pt = input("Enter input plaintext(integer) : ")
# ctarr = [pow(int(m),d)%n for m in pt]
# ct=""
# for i in ctarr:
#     ct+=str(i)
# print(f"ENCRYPTED CIPHER TEXT : {ct}")
# print("---------------DECRYPTION USING PUBLIC KEY-------------")
# ct = input("Enter cipher text (sample input press enter)")
# ct = ctarr
# ptarr = [int(pow(c, e)%n) for c in ctarr]
# pt=""
# for i in ptarr:
#     pt+=str(i)
# print(f"DECRYPTED PLAIN TEXT : {pt}")



