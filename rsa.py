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
print("---------------ENCRYPTION-------------")
pt = input("Enter input plaintext(integer) : ")
ctarr = [pow(int(m),e)%n for m in pt]
print(f"ENCRYPTED CIPHER TEXT : {ctarr}")
print("---------------DECRYPTION-------------")
ct = input("Enter cipher text (sample input press enter)")
ct = ctarr
ptarr = [int(pow(c, d)%n) for c in ctarr]
pt=""
for i in ptarr:
    pt+=str(i)
print(f"DECRYPTED PLAIN TEXT : {pt}")