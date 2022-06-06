print("-----------PRIMITIVE ROOT--------------")
def gcd(x, y):
    small, large = (x, y) if x<y else (y,x)
    while small!=0:
        temp=large%small
        large=small
        small=temp
    return large
    
def findPrimitive(n):
    roots=[]
    required_set = set(num for num in range(1, n) if gcd(num, n)==1)
    print(f"required_set : {required_set}")
    for g in range(1, n):
        actual_set = set(pow(g, powers)%n for powers in range(1, n))
        print(f"For g={g}, actual set is : {actual_set}")
        if required_set==actual_set:
            print("----------------------------------------------------")
            print(f"For g={g} actual_set==required_set hence appending {g} in roots")
            print("----------------------------------------------------")
            roots.append(g)
    print(f"roots are {roots}")
    print("--------------PRIMITIVE ROOTS FOUND---------------------")
    return min(roots)

P = int(input("Enter value of P : ")) #23
# A primitive root for P, G is taken
alpha = findPrimitive(P)
# alpha = int(input("Enter primitive root of P : "))
print("---------------DEFFIE HELLMAN ALGORITHM-------------")
print('The Value of P(prime no.) is :%d'%(P))
print('The Value of G(primitive root) is :%d'%(alpha))
# Alice will choose the private key a
xa = int(input("Enter private key of Alice : ")) #4
# Bob will choose the private key b
xb = int(input("Enter private key of Bob : ")) #3
print("-----------------------------------------")
print('The Private Key xa for Alice is :%d'%(xa))
# gets the generated key
ya = int(pow(alpha,xa,P))
print(f"Public key of Bob is {ya}")

print('The Private Key xb for Bob is :%d'%(xb))
# gets the generated key
yb = int(pow(alpha,xb,P))
print(f"Public key of Bob is {yb}")
print("-----------------------------------------")
# Secret key for Alice
ka = int(pow(yb,xa,P))
# Secret key for Bob
kb = int(pow(ya,xb,P))
print('Secret key for the Alice is : %d'%(ka))
print('Secret Key for the Bob is : %d'%(kb))
if(ka==kb):
    print("Both keys are equal hence key sharing is successful using Deffie-Hellman algorithm !")
# P = int(input("Enter value of P : ")) #23
# # A primitive root for P, G is taken
# # alpha = findPrimitive(P)
# alpha = int(input("Enter primitive root of P : "))
# print("---------------DEFFIE HELLMAN ALGORITHM-------------")
# print('The Value of P(prime no.) is :%d'%(P))
# print('The Value of G(primitive root) is :%d'%(alpha))
# # Alice will choose the private key a
# xa = int(input("Enter private key of Alice : ")) #4
# # Bob will choose the private key b
# xb = int(input("Enter private key of Bob : ")) #3
# print("-----------------------------------------")
# print('The Private Key xa for Alice is :%d'%(xa))
# # gets the generated key
# ya = int(pow(alpha,xa,P))
# print(f"Public key of Bob is {ya}")

# print('The Private Key xb for Bob is :%d'%(xb))
# # gets the generated key
# yb = int(pow(alpha,xb,P))
# print(f"Public key of Bob is {yb}")
# print("-----------------------------------------")
# # Secret key for Alice
# ka = int(pow(yb,xa,P))
# # Secret key for Bob
# kb = int(pow(ya,xb,P))
# print('Secret key for the Alice is : %d'%(ka))
# print('Secret Key for the Bob is : %d'%(kb))
# if(ka==kb):
#     print("Both keys are equal hence key sharing is successful using Deffie-Hellman algorithm !")