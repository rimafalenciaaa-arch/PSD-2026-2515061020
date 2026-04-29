## Sistem Pembelian Buku (LinkedList)
# A. Judul Program
Sistem Pembelian Buku dengan menggunakan LinkedList

# Deskripsi Singkat
Program ini dibuat untuk mengelola daftar pembelian buku dengan menggunakan Linked List. User dapat menambahkan pembelian, melihat daftar pembelian, dan memproses pembelian.

Algoritma yang digunakan adalah Single LinkedList. Algoritma ini menggunakan konsep FIFO (First In First Out), di mana pembelian yang pertama masuk akan diproses terlebih dahulu.

# Source Code
<img width="991" height="617" alt="image" src="https://github.com/user-attachments/assets/e6514c76-0204-4309-b712-08a29523171e" />
<img width="1082" height="603" alt="image" src="https://github.com/user-attachments/assets/525c22cf-befa-4d9a-9ef1-28d3cd5cb516" />
<img width="1097" height="612" alt="image" src="https://github.com/user-attachments/assets/b6774802-9678-4cb5-baf6-8c7f930495a7" />
<img width="1103" height="611" alt="image" src="https://github.com/user-attachments/assets/79aca336-71e2-453b-95e4-d7f3aef2a153" />

# Penjelasan Kode
1. Class Node
Digunakan membuat/mengklasifikasikan objek. dalam program ini digunakan untuk menyimpan data pembelian
Memiliki atribut seperti:
pembelian → menyimpan daftar nama buku
next → menunjuk ke node berikutnya

2. Class LinkedList
__init__()
* Menginisialisasi head sebagai None/memberikan nilai awal
* tambah_pembelian(pembelian) : Membuat node baru
* Jika list kosong → akan menjadi head
* Jika tidak kosong → akan ditambahkan di akhir

* tampilkan_pembelian() : Menampilkan semua data dengan perulangan dari head sampai akhir

* proses_pembelian() : Menghapus node pertama (head) dan memindahkan ke node berikutnya

3. Fungsi menu()
4. Menampilkan pilihan menu ke user

5. Fungsi main()
Menggunakan perulangan while True
Input user diproses dengan try-except
Menjalankan fungsi sesuai pilihan menu

# Output Program
<img width="931" height="850" alt="image" src="https://github.com/user-attachments/assets/6115f08e-0507-4edb-a81f-fb9ac4aba605" />
<img width="931" height="853" alt="image" src="https://github.com/user-attachments/assets/7c5ae6d7-b26c-4bc9-acc9-1a1256922da0" />
<img width="917" height="399" alt="image" src="https://github.com/user-attachments/assets/d1b3f4f0-6508-4482-85e3-5bde30f59059" />

# Penjelasan Output
* Saat user memasukkan huruf (bukan angka) → muncul pesan "Input harus angka!"
* Saat memilih menu yang tidak tersedia/tidak ada dalam kode program → muncul "Pilihan tidak valid!"
* Saat menambah pembelian → data akan masuk ke Linked List
* Saat menampilkan → semua pesanan ditampilkan berurutan
* Saat memproses data pemeblian → pesanan pertama dihapus (FIFO)

# Link Youtube
https://youtu.be/eCIdhGwSma4





