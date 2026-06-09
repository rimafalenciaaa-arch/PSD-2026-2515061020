## Judul Progrram
Implementasi Hash Map Menggunakan Metode Separate Chaining pada Python

## Deskripsi Singkat
Program ini merupakan implementasi Hash Map menggunakan metode Separate Chaining untuk menangani collision (tabrakan data) pada proses hashing. Hash Map adalah struktur data yang digunakan untuk menyimpan pasangan key-value sehingga proses penyimpanan dan pencarian data dapat dilakukan dengan cepat.

## Source Code
<img width="898" height="626" alt="image" src="https://github.com/user-attachments/assets/53d73138-37ee-4174-83b2-b345ef913642" />
<img width="1018" height="641" alt="image" src="https://github.com/user-attachments/assets/ea818b66-d4ad-43dd-966c-a15c6078c880" />
<img width="808" height="583" alt="image" src="https://github.com/user-attachments/assets/ac3cbeda-42c2-4075-a097-e7d3add77cc1" />

Penjelasan Code

class Node:
- Membuat class Node yang digunakan sebagai elemen pada linked list.

def __init__(self, key, value):
- Constructor untuk menginisialisasi objek node.

self.key = key
- Menyimpan nilai key.

self.value = value
- Menyimpan nilai value.

self.next = None
- Pointer ke node berikutnya, awalnya kosong.

class HashMap:
- Membuat class utama Hash Map.

def __init__(self, size=5):
- Constructor untuk menentukan ukuran tabel hash.

self.size = size
- Menyimpan ukuran tabel hash.

self.table = [None] * size
- Membuat tabel hash dengan isi awal None.

def hash_function(self, key):
- Fungsi untuk menentukan indeks penyimpanan data.

return key % self.size
- Menggunakan operasi modulo untuk menghasilkan indeks hash.

def insert(self, key, value):
-  Digunakan untuk menambahkan data ke Hash Map.

index = self.hash_function(key)
- Menghitung indeks berdasarkan key.

new_node = Node(key, value)
- Membuat node baru.

new_node.next = self.table[index]
- Node baru menunjuk ke node lama pada indeks tersebut.

self.table[index] = new_node
- Node baru menjadi node pertama pada chain.

def search(self, key):
- Digunakan untuk mencari data berdasarkan key.

index = self.hash_function(key)
- index = self.hash_function(key)

current = self.table[index]
- Mengambil node pertama pada indeks tersebut.

while current:
- Melakukan penelusuran linked list.

if current.key == key:
- Mengecek apakah key ditemukan.

return current.value
- Mengembalikan value yang sesuai.

current = current.next
- Berpindah ke node berikutnya.

return None
- Jika data tidak ditemukan.

def display(self):
- Menampilkan seluruh isi Hash Map.

for i in range(self.size):
- Melakukan perulangan pada setiap indeks tabel hash.

current = self.table[i]
- Mengambil node pada indeks tersebut.

while current:
- Menelusuri seluruh linked list pada indeks.

print(f"({current.key},{current.value}) -> ", end="")
- Menampilkan pasangan key dan value.

current = current.next
- Berpindah ke node berikutnya.

print("NULL")
- Menandakan akhir linked list.

def main():
- Fungsi utama program.

hm = HashMap()
- Membuat objek Hash Map.

hm.insert(1, "Andre")
hm.insert(6, "Tio")
hm.insert(11, "Rani")
- Menambahkan data ke Hash Map.

hm.display()
- Menampilkan seluruh isi Hash Map.

## Output Program
<img width="770" height="326" alt="image" src="https://github.com/user-attachments/assets/e6df5c6e-bcc5-4b9b-b713-d9aced576465" />

Penjelasan Output

Isi Hash Map:

0: NULL
1: (11,Rani) -> (6,Tio) -> (1,Andre) -> NULL
2: NULL
3: NULL
4: NULL

- Program terlebih dahulu menampilkan seluruh isi tabel hash yang memiliki ukuran 5 indeks (0–4).

Cari key: 11
- Pengguna memasukkan key 11 yang ingin dicari.

Data ditemukan yaitu Rani

## Link Youtube

https://youtu.be/HipzBvHRRXU





