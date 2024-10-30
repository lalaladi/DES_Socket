import socket
import os
from des_ctr import message_to_encrypt

def generate_key():
    """Menghasilkan kunci 8 byte secara acak"""
    return os.urandom(8)

# Pesan yang ingin dikirim
plaintext = input("Masukkan teks yang ingin dikirim: ")

sKey = generate_key()  # Menghasilkan kunci baru
print("Kunci yang digunakan: ", sKey)
encrypt_message = message_to_encrypt(plaintext, sKey)
print(f"Hasil Enkripsi:{encrypt_message}")

# Mengonversi ciphertext ke byte untuk dikirim
encrypted_message = sKey + bytes(encrypt_message)

# Membuat socket dan mengirim pesan terenkripsi
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender_socket.connect(('localhost', 12222))
sender_socket.send(encrypted_message)

sender_socket.close()
