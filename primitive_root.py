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

n = int(input("Enter prime no : "))
findPrimitive(n)