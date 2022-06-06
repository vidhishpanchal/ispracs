from Crypto.Cipher import AES
import binascii, os

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

secretKey = os.urandom(32)  # 256-bit random encryption key
print("Encryption key:", binascii.hexlify(secretKey))
msg = input("Enter message to encrypt : vidhishpanchal")
msg = "vidhishpanchal"
# msg = b'Message for AES-256-GCM + Scrypt encryption'
encryptedMsg = encrypt_AES_GCM(msg.encode(), secretKey)
# print("encryptedMsg", {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'aesIV': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2])
# })

decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
print("decryptedMsg", decryptedMsg)







# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# data = input("Enter data : ")
# key = get_random_bytes(16)
# print(f"Key : {key}")
# cipher = AES.new(key, AES.MODE_EAX)
# ciphertext, tag = cipher.encrypt_and_digest(data.encode())
# print(cipher.hexdigest())
