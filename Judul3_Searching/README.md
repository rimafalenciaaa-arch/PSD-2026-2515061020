## A. Judul Program
Mencari suatu nilai dengan menggunakan BinarySearch

## Deskripsi Singkat
Program ini dibuat untuk mencari suatu nilai dengan menggunakan metode Binary Search dalam bahasa Python. Program meminta pengguna atau user untuk memasukkan data suatu nilai yang sudah diurutkan, lalu mencari nilai tertentu dengan cara membandingkan nilai di tengah data secara terus-menerus hingga nilai tersebut ditemukan. Dengan metode BinarySearch ini membuat proses pencarian menjadi lebih cepat.

## Source Code
<img width="856" height="889" alt="image" src="https://github.com/user-attachments/assets/0e7b3727-bc07-4b78-89df-fe3b7424976a" />
<img width="752" height="364" alt="image" src="https://github.com/user-attachments/assets/ccc9f651-b9de-49eb-8e48-35b2f409ed38" />

Penjelasan Code:

def binary_search(arr, target): : Mendefinisikan fungsi bernama binary_search.

l = 0: Membuat variabel l (left) sebagai batas indeks paling kiri, dimulai dari 0.

r = 1: Sebagai batas indeks paling kanan.

pos = -1 : -1 akan dimasukkan ke variabel pos

while l <= r: : Perulangan akan terus berjalan selama batas kiri belum melewati batas kanan.

m = l + (r - l) // 2: Mencari nilai tengah atau median

print(f"Median: {m}, nilai: {arr[m]}"): Mencetak indeks tengah dan nilai yang ada di indeks tersebut.

if arr[m] == target:: Mengecek apakah nilai di indeks tengah sama dengan target yang dicari.

pos = m & break: Jika sama, simpan indeks tersebut ke variabel pos dan segera hentikan perulangan.

elif arr[m] < target:: Jika nilai di tengah lebih kecil dari target.

print("Mencari nilai di kanan") & l = m + 1: Pencarian pindah ke kanan dan geser batas kiri ke depan indeks tengah.

else: : Jika nilai di tengah lebih besar dari target.

print("Mencari nilai di kiri") & r = m - 1: Pencarian pindah ke kiri dan geser batas kanan ke belakang indeks tengah.

return pos: Mengirimkan hasil akhir (indeks target atau -1) keluar dari fungsi.


def main(): Merupakan fungsi utama

try: : Memulai blok pengecekan kesalahan.

n = int(input("Masukkan jumlah nilai: ")): Meminta input berapa banyak angka yang ingin dimasukkan dan mengubahnya menjadi tipe integer (bilangan bulat).

except ValueError: : Jika pengguna memasukkan teks atau simbol (bukan angka), tampilkan pesan error dan hentikan program dengan return.

arr = []: Membuat list kosong untuk menampung angka yang akan diinput.

print("Masukkan nilai (urut menurun):") : Instruksi kepada pengguna.

for i in range(n): : Melakukan perulangan sebanyak n kali.

while True: : Perulangan "abadi" yang baru akan berhenti (break) jika pengguna memasukkan angka yang valid.

nilai = int(input()): Mengambil input angka dari pengguna.

arr.append(nilai): Memasukkan angka yang baru saja diketik ke dalam list arr.

print(f"Array: {arr}"): Menampilkan list angka yang sudah berhasil dikumpulkan.

target = int(input("Masukkan angka yang ingin dicari: ")): Meminta satu angka terakhir yang ingin dicari posisinya.

pos = binary_search(arr, target): Memanggil fungsi binary_search dengan data yang sudah ada dan menyimpan hasilnya di variabel pos.

if pos != -1: : Jika nilai pos tidak sama dengan -1" (artinya target ditemukan).

print(f"Ditemukan pada indeks ke-{pos}"): Mencetak posisi indeks angka tersebut.

else: : Jika pos tetap -1 (artinya target tidak ditemukan).

print("Tidak ditemukan"): Memberikan informasi bahwa angka tersebut tidak ada di dalam list.

if __name__ == "__main__": main(): Untuk menjalankan program

## Output Program
<img width="1082" height="337" alt="image" src="https://github.com/user-attachments/assets/f3336447-9cfb-428b-a879-f191a499a485" />

Penjelasan Output

Masukkan jumlah nilai: 6 : Menginputkan nilai yang ingin dimasukkan

Masukkan nilai (urut menurun): : Menginputkan nilai yang sudah terurut

Array: [11, 9, 8, 4, 3, 1] : Memberikan output sesuai dengan yang diinputkan

Ditemukan pada indeks ke-0 : Memberikan output sesuai dengan indeks yang ditemukan

## Link Youtube
https://youtu.be/uT00ctpIyEM56




