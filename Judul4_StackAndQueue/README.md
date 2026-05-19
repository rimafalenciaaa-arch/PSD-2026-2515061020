## A. Judul Program
Program Stack Menggunakan Array dengan Python

## Deskripsi Singkat
Program ini dibuat untuk mengelola data menggunakan struktur data Stack dengan bahasa pemrograman Python. Stack bekerja dengan konsep LIFO (Last In First Out), yaitu data yang terakhir masuk akan menjadi data pertama yang keluar. Program memiliki beberapa fitur seperti menambahkan data (push), menghapus data (pop), dan menampilkan isi stack.

## Source Code
<img width="829" height="688" alt="image" src="https://github.com/user-attachments/assets/45021737-56f0-44ba-9512-a70070f0e39c" />
<img width="881" height="797" alt="image" src="https://github.com/user-attachments/assets/aba64cd5-d9a3-48a1-94fa-120a33608056" />

Penjelasan Kode

class Stack:
- Membuat class bernama Stack.

def __init__(self, ukuran=10):
- Fungsi yang otomatis berjalan saat objek Stack dibuat. Fungsi ini menerima parameter ukuran dengan nilai default 10 jika tidak ditentukan.

self.data = [0] * ukuran
- Membuat list/array berisi angka 0 sebanyak ukuran stack.

self.top = -1
- Menandakan stack masih kosong karena belum ada data.

 self.ukuran = ukuran
 - Menyimpan kapasitas maksimum stack.

def push(self, nilai):
- untuk menambahkan data ke stack.

if self.top == self.ukuran - 1:
- Mengecek apakah stack sudah penuh.

print("Stack penuh")
- Menampilkan pesan jika stack penuh.

self.top += 1
- Posisi top naik satu.

self.data[self.top] = nilai
- Menyimpan nilai ke posisi top.

print(f"{nilai} ditambahkan")
- Menampilkan pesan data berhasil ditambahkan.

def pop(self):
- untuk menghapus data teratas stack.

if self.top == -1:
- Mengecek apakah stack kosong.

print(f"{self.data[self.top]} dihapus")
- Menampilkan data yang dihapus.

self.top -= 1
- Top turun satu setelah data dihapus.

 def tampil(self):
 - untuk menampilkan isi stack.

if self.top == -1:
- Mengecek apakah stack kosong.

print("Isi stack:", end=" ")
- Menampilkan tulisan “Isi stack:”.

for i in range(self.top, -1, -1):
- Perulangan dari data paling atas ke bawah.

 print(self.data[i], end=" ")
 - Menampilkan isi stack.

while True:
- Perulangan menu terus berjalan sampai user keluar.

 print("\n=== MENU STACK ===")
 - Menampilkan judul menu.

 print("1. Push")
 print("2. Pop")
 print("3. Tampil")
 print("4. Keluar")
 - Menampilkan pilihan menu.

pilih = int(input("Pilih: "))
- Meminta input pilihan user.

if pilih == 1:
- Jika user memilih menu push.

nilai = int(input("Masukkan nilai: "))
- Input data yang ingin ditambahkan.

s.push(nilai)
- Memanggil fungsi push.

elif pilih == 2:
- Jika user memilih pop

s.pop()
- Memanggil fungsi pop.

elif pilih == 3:
- Jika user memilih tampil.

s.tampil()
- Menampilkan isi stack.

elif pilih == 4:
- Jika user memilih keluar.

print("Program selesai")
- Menampilkan pesan program selesai.

break
- Menghentikan perulangan.

print("Pilihan salah")
- Menampilkan pesan error.

if __name__ == "__main__":
main()
- Untuk menjalankan program.

## Output Program
<img width="815" height="640" alt="image" src="https://github.com/user-attachments/assets/37299854-c4dc-4fb0-b2ee-c758d1f417ee" />
<img width="777" height="611" alt="image" src="https://github.com/user-attachments/assets/06c0c815-207b-4106-9a14-f7fc9421c247" />

Program menampilkan menu:
1. Push → menambah data
2. Pop → menghapus data teratas
3. Tampil → menampilkan isi stack
4. Keluar → keluar dari program

Pengguna memilih:
Pilih: 1

Artinya pengguna memilih menu Push.

Program meminta input nilai:

Masukkan nilai: 1

Setelah nilai dimasukkan, program menambahkan data ke stack lalu menampilkan:

1 ditambahkan

Langkah yang sama dilakukan lagi untuk nilai:
2
3
4

Semua data berhasil masuk ke stack secara berurutan.

Urutan isi stack menjadi:

4  ← paling atas
3
2
1

Karena stack menggunakan konsep LIFO (Last In First Out), maka data terakhir yang masuk (4) akan menjadi data pertama yang keluar jika dilakukan Pop.

Terakhir pengguna memilih:
Pilih: 4

Artinya memilih menu keluar, sehingga program menampilkan:

Program selesai

dan program berhenti dijalankan.

## Link Youtube
https://youtu.be/T3D-YwkbR1g


































