from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import logging

# Set up basic logging
logging.basicConfig(filename='vault.log', level=logging.INFO)

# Generate a random 256-bit key and IV
key = get_random_bytes(32)
iv = get_random_bytes(16)

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    return data[:-data[-1]]

def encrypt_file():
    with open("vault.txt", "w") as f:
        f.write("Secret data inside vault.")

    data = open("vault.txt", "rb").read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data))

    with open("vault.txt.enc", "wb") as f:
        f.write(iv + encrypted)

    logging.info("Encrypted vault.txt -> vault.txt.enc")
    print("Encrypted vault.txt")

def decrypt_file():
    with open("vault.txt.enc", "rb") as f:
        iv_read = f.read(16)
        encrypted = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv_read)
    decrypted = unpad(cipher.decrypt(encrypted))

    with open("vault_decrypted.txt", "wb") as f:
        f.write(decrypted)

    logging.info("Decrypted vault.txt.enc -> vault_decrypted.txt")
    print("Decrypted vault.txt.enc")

if __name__ == "__main__":
    encrypt_file()
    decrypt_file()
