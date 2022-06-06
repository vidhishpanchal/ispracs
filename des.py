from des import DesKey
key0 = DesKey(b"some key") 
m = input("Enter message : ")
ct = key0.encrypt(m.encode(), initial=0, padding=True)
print(f"Encrypted message : {ct}")
ciphertext = input(f"Enter message to be decrypted : {ct}")
ciphertext=ct
pt = key0.decrypt(ct.encode(), padding=True)

