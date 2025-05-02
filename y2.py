from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    with open(file_path + '.enc', 'wb') as enc_file:
        enc_file.write(cipher.iv)          # Write IV
        enc_file.write(encrypted_data)

    os.remove(file_path)                   # Remove original file
    print(f"Encrypted: {file_path}")

def generate_key():
    return get_random_bytes(16)            # AES key size 128 bits

if __name__ == "__main__":
    key = generate_key()                   # Generate AES key

    files = ['file1.txt', 'file2.docx']    # Add file names you want to encrypt
    for file in files:
        encrypt_file(file, key)