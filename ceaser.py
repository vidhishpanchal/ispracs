def encrypt():
    pt = input("Enter plaintext : ")
    key = int(input("Enter integer key : "))
    ptarr = []
    ct=""
    for i in pt:
        m = chr(ord(i)+key)
        ptarr.append(m)
        ct+=m
    print(f"ENCRYPTED CIPHER TEXT : {ct}")

def decrypt():
    ct = input("Enter cipher text : ")
    key = int(input("Enter integer key : "))
    ctarr = [c for c in ct]
    ptarr=[]
    pt=""
    for c in ct:
        m = chr(ord(c)-key)
        ptarr.append(m)
        pt+=m
    print(f"DECRYPTED PLAINTEXT IS : {pt}")

print("-------------CEASER CIPHER-------------")
print("1) Encrpyt\n2) Decrypt\n3) Exit\n")
choice = int(input("Enter choice : "))
if choice==1:
    encrypt()
elif choice==2:
    decrypt()
elif choice==3:
    print("Goodbye")