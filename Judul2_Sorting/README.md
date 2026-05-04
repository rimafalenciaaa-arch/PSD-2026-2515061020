## a. Judul Program
Sistem Harga Makanan Menggunakan Insertion Sort
## b. Deskripsi Singkat
Program ini digunakan untuk mengurutkan harga makanan dari harga paling tinggi ke paling rendah (descending) dengan menggunakan algoritma Insertion Sort. Pengguna memasukkan harga makanan, lalu program akan menampilkan data sebelum dan sesudah diurutkan.
## c. Source Code
Screenshoot source code:
<img width="576" height="508" alt="image" src="https://github.com/user-attachments/assets/c3b2837a-621f-4054-9b1b-1e8c76555ca3" />
<img width="731" height="396" alt="image" src="https://github.com/user-attachments/assets/910acaba-af4e-4ac0-b87e-a4980703d591" />

Penjelasan Code

- def insertion_sort(jumlah, n): ini merupakan fungsi dari insertion sort nya

- for i in range(1, n) : ini merupakan perulangan dimulai dari indeks ke-1 sampai ke n.

- temp = jumlah[i] : jumlah indeks akan disimpan ke variabel temp

- j = i - 1 : elemen akan menggeser elemen ke kiri.

- while j >= 0 and jumlah[j] < temp : ini merupakan fungsi descending (dari besar ke kecil)

- jumlah[j + 1] = jumlah[j] : menggeser nilai yang lebih kecil ke posisi kanan.

- j -= 1: pengecekan berlanjut ke elemen di sebelah kirinya lagi.

- jumlah[j + 1] = temp: setelah menemukan posisi yang tepat, masukkan nilai temp ke posisi tersebut.


- def main(): untuk menjalankan fungsi nya

- n = int(input("Masukkan jumlah makanan: ")) : meminta input jumlah data dan mengubahnya menjadi tipe data integer.

- except ValueError: jika input bukan angka (misal: huruf), bagian ini akan dijalankan.

- print("Input tidak valid!") & return: memberi pesan error dan menghentikan program.

- jumlah = [] : membuat list kosong untuk menampung harga makanan.

- for i in range(n) : perulangan sebanyak n kali untuk mengambil input harga.

- jumlah.append(nilai): menambahkan angka tersebut ke dalam list jumlah.

- break: keluar dari while True karena input sudah berhasil masuk.

- print(f"Harga sebelum diurutkan: {jumlah}"): menampilkan list harga asli sebelum diproses.

- print("Harga setelah diurutkan (Insertion Sort):", end=" "): menampilkan harga setelah diurutkan

- for i in range(n): print(jumlah[i], end=" "): melakukan perulangan untuk mencetak setiap angka yang sudah terurut satu per satu secara menyamping.


- if __name__ == "__main__": main(): untuk menjalankan program

## d. Output Program
<img width="802" height="260" alt="image" src="https://github.com/user-attachments/assets/04a4370b-d743-46f3-9498-60adf5da793e" />

Penjelasan Ouput

- Memasukkan jumlah dan harga makanan

- Harga sebelum diurutkan: [13, 19, 21, 9] : maka akan menampilkan input harga asli nya

- Harga setelah diurutkan (Insertion Sort): 21 19 13 9 : maka akan mnenampilkan harga setelah diurutkan berdasarkan harga tertinggi ke terendah

## e. Link Youtube
https://youtu.be/VjUFhzHo33A
