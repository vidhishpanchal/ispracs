def encrypt():
    print("-------------ENCRYPTION-------------")
    pt = input("Enter plain text : ")
    ptarr = [i for i in pt]
    noofrows = int(input("Enter number of rows : "))
    matrix=[]
    ctarr=[]
    for i in range(0,len(pt),noofrows):
        m = ptarr[i:i+noofrows]
        matrix.append(m)
    print(matrix)
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            ctarr.append(matrix[j][i])
        ctarr.append("@")
    ct=""
    for i in ctarr:
        ct+=i
    print(f"ENCRYPTED CIPHER TEXT : {ct}")
        
def decrypt():
    print("-------------DECRYPTION-------------")
    ct = input("Enter cipher text : ad@be@cf@ (test input)")
    ct = "ad@be@cf@"
    ctarr = [i for i in ct]
    ptarr=[]
    temp=[]
    matrix=[]
    print(ctarr)
    for c in ctarr:
        if c!="@":
            temp.append(c)
        else:
            matrix.append(temp)
            temp=[]
    print(matrix)
    l = len(matrix)
    ans=[]
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            ans.append(matrix[j][i])
    pt=""
    for i in ans:
        pt+=i
    print(f"DECRYPTED PLAIN TEXT IS : {pt}")
    
    # for i in 
print("-------------COLUMNAR TRANSPOSITION-------------")
print("1) Encrpyt\n2) Decrypt\n3) Exit\n")
choice = int(input("Enter choice : "))
if choice==1:
    encrypt()
elif choice==2:
    decrypt()
elif choice==3:
    print("Goodbye")