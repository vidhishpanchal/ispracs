import math
# helper functions
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
def rightrotate(s, d):
    return leftrotate(s, len(s) - d)
def counterClockspiralPrint(m, n, arr) :
    k = 0; l = 0
    ans=[]
    ansstr=""
    # k - starting row index
    # m - ending row index
    # l - starting column index
    # n - ending column index
    # i - iterator
    # initialize the count
    cnt = 0
    # total number of
    # elements in matrix
    total = m * n
    while (k < m and l < n) :
        if (cnt == total) :
            break
        # Print the first column
        # from the remaining columns
        for i in range(k, m) :
            # print(arr[i][l], end = " ")
            ans.append(arr[i][l])
            cnt += 1
        l += 1
        if (cnt == total) :
            break
        # Print the last row from
        # the remaining rows
        for i in range (l, n) :
            # print( arr[m - 1][i], end = " ")
            ans.append(arr[m - 1][i])
            cnt += 1
        m -= 1
        if (cnt == total) :
            break
        # Print the last column 
        # from the remaining columns
        if (k < m) :
            for i in range(m - 1, k - 1, -1) :
                # print(arr[i][n - 1], end = " ")
                ans.append(arr[i][n-1])
                cnt += 1
            n -= 1
        if (cnt == total) :
            break
        # Print the first row
        # from the remaining rows
        if (l < n) :
            for i in range(n - 1, l - 1, -1):
                # print( arr[k][i], end = " ")
                ans.append(arr[k][i])
                cnt += 1
            k += 1
        return ans

def spiralPrintClockwise(m, n, a):
    k = 0
    l = 0
    ans=[]
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            # print(a[k][i], end=" ")
            ans.append(a[k][i])
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            # print(a[i][n - 1], end=" ")
            ans.append(a[i][n - 1])
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n - 1, (l - 1), -1):
                # print(a[m - 1][i], end=" ")
                ans.append(a[m - 1][i])
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                # print(a[i][l], end=" ")
                ans.append(a[i][l])
            l += 1
        return ans
 
#-----------------------------------------------------------------------
def encrypt(plaintext, key):
    asciivalueofpt=[]
    s=""
    # pass through S-BOX
    print("--------------------PASS THROUGH S-BOX---------------------")
    # adding index + 1 to ascii value
    for i in plaintext:
        s+=chr(ord(i)+plaintext.index(i)+1)
    print("1) Added index plus one to ascii value : ", s)
    # swap in pairs
    s = list(s)
    for i in range(0, len(s)-1, 2):
        s[i], s[i+1] = s[i+1], s[i]
    s=''.join(s)
    print("2) Swap in pairs : ", s)
    # rotate the string by key
    s = leftrotate(s, key)
    print("3) Rotating by key : ", s)
    print("\n--------------------PASS THROUGH P-BOX---------------------")
    matrix=[]
    temp=[]
    indexofi=0
    for i in range(math.floor(len(s)/3)):
        for j in range(0,3):
            temp.append(s[indexofi])
            indexofi+=1
        matrix.append(temp)
        temp=[]
    print("4) Matrix after columnar split : ", matrix)
    anticlockwisespiral = counterClockspiralPrint(2, 3, matrix)
    print("5) Anticlockwise spiral traversal", anticlockwisespiral)
    for i in anticlockwisespiral:
        if i==" ":
            i="@"
    print("6) Place @ in place of spaces : ", anticlockwisespiral)
    newstr = ""
    for i in anticlockwisespiral:
        newstr+=i
    s = leftrotate(newstr, key)
    print("7) Left rotate by key : ", s)
    matrix=[]
    temp=[]
    indexofi=0
    for i in range(math.floor(len(s)/3)):
        for j in range(0,3):
            temp.append(s[indexofi])
            indexofi+=1
        matrix.append(temp)
        temp=[]
    print("8) Array again converted to matrix : ", matrix)
    clockwisespiraltraversal = spiralPrintClockwise(2, 3, matrix)
    print("9) Clockwise spiral traversal of matrix : ",clockwisespiraltraversal)
    s=""
    for i in clockwisespiraltraversal:
        s+=i
    print("\n Therefore, the encrypted message is : ", s)
    
        
def decrypt(ciphertext, key):
    print("----------------DECRYPTION----------------")
    print("\n--------------REVERSAL OF P-BOX--------------")
    #anticlockwise spiral traversal
    matrix=[]
    temp=[]
    indexofi=0
    for i in range(math.floor(len(ciphertext)/3)):
        for j in range(0,3):
            temp.append(ciphertext[indexofi])
            indexofi+=1
        matrix.append(temp)
        temp=[]
    reverseclockwisespiral = spiralPrintClockwise(2, 3, matrix)
    print("1) Reverse of clockwise spiral traversal : ", reverseclockwisespiral)
    newstr=""
    for i in reverseclockwisespiral:
        newstr+=i
    s = leftrotate(newstr, -1*key)
    print("2) Reverse left rotate by key : ", s)
    for i in range(0, len(s)):
        if s[i]=="@":
            s[i]==" "
    print("3) Put space in place of @ : ", s) 
    print("\n--------------REVERSAL OF S-BOX--------------")
    #Reverse of anticlockwise
    s="hfljdb"
    
    print("4) Reverse of anticlockwise : ", s)
    #rorate by key * -1
    newstr=""
    for i in s:
        newstr+=i
    s = leftrotate(newstr, -1*key)
    print("5) Reverse left rotate by key : ", s)
    #swap in pairs
    s = list(s)
    for i in range(0, len(s)-1, 2):
        s[i], s[i+1] = s[i+1], s[i]
    s=''.join(s)
    print("6) Swap in pairs back again : ", s)
    # adding index + 1 to ascii value
    newstr=""
    for i in s:
        newstr+=chr(ord(i)-s.index(i)-1)
    print("7) Reversed adding index plus one to ascii value : ", newstr)
    print("\nTherefore the decrypted plaintext is : ", newstr)
    
#dbljhf    
print("1)Encrypt\n2)Decrypt\n3)Exit")
choice = int(input("\nEnter your choice : "))
if choice==1:
    plaintext=input("Enter plaintext : ")
    key = int(input("Enter key : "))
    encrypt(plaintext, key)
elif choice==2:
    ciphertext="dbljhf "
    print("Enter ciphertext : dbljhf")
    # ciphertext=input("Enter ciphertext : dbljhf")
    key = int(input("Enter key : "))
    decrypt(ciphertext, key)
elif choice==3:
    print("OK Exiting")
else:
    print("Please provide a number from above.\nExiting")