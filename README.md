# Tugas 2 Keamanan Informasi

## Pengembangan Implementasi Enkripsi dan Dekripsi DES
1. Implementasi transfer string terenkripsi antar 2 user menggunakan socket programming (penerima dapat mendekripsi string dari pengirim)
2. Enkripsi dan Dekripsi harus bisa menerima input lebih dari 64bit (8 karakter)
3. String enkripsi wajib dikirimkan melalui socket (tidak boleh read/write file)
4. Untuk key dianggap 2 client tau(boleh hardcode)


## Pembagian Tugas Anggota Kelompok

| Nama                      | NRP         | Pembagian Kerja |
|---------------------------|-------------|------------------|
| Dian Lies Seviona Dabukke | 5025211080  | <ul><strong>`sender.py`</strong><li>Menghasilkan Kunci Acak (Key): Menambahkan fungsi `generate_key()` untuk membuat kunci DES secara acak setiap kali pesan dikirim, sehingga keamanan pesan meningkat.</li><li>Enkripsi Pesan: Mengimplementasikan fungsi `message_to_encrypt()` dari `des_ctr` untuk mengubah pesan plaintext menjadi ciphertext menggunakan mode Counter (CTR).</li><li>Menggabungkan Kunci dengan Pesan Terenkripsi: Menggabungkan kunci acak yang digunakan dengan pesan terenkripsi untuk dikirim bersama melalui socket.</li><li>Pengujian Enkripsi dan Pengiriman: Menjalankan pengujian untuk memastikan pesan yang dikirim sudah benar-benar terenkripsi dan diterima oleh receiver.</li></ul> |
| Shafa Nabilah Hanin       | 5025211222  | <ul><strong>`receiver.py`</strong><li>Menerima Pesan melalui Socket: Mengimplementasikan bagian socket untuk mendengarkan dan menerima pesan dari sender.</li><li>Memisahkan Kunci dan Pesan: Mengambil kunci yang digunakan dari 8 byte pertama data yang diterima, dan mengidentifikasi bagian pesan yang terenkripsi.</li><li>Dekripsi Pesan: Menggunakan fungsi `message_to_decrypt()` dari `des_ctr` untuk mendekripsi pesan yang diterima dengan kunci yang sama dari sender.</li><li>Pengujian Penerimaan dan Dekripsi: Menguji program untuk memastikan pesan yang diterima sama dengan pesan asli sebelum enkripsi.</li></ul> |
