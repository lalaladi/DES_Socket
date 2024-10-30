import socket
from des_ctr import message_to_decrypt

# Membuat socket dan menerima pesan
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.bind(('localhost', 12222))
receiver_socket.listen(1)
print("Menunggu koneksi...")
conn, addr = receiver_socket.accept()

# Menerima dan mendekripsi pesan
data_received = conn.recv(1024)  # Terima pesan terenkripsi

# Memisahkan kunci dan pesan
sKey_received = data_received[:8]         # 8 byte pertama adalah kunci
message_received = data_received[8:]      # Sisanya adalah pesan
print("Pesan yang diterima:",message_received)

decrypted_message = message_to_decrypt(message_received, sKey_received)

receiver_socket.close()
