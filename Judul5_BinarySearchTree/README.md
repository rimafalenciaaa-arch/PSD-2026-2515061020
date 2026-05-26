## Judul Program
Program Binary Search Tree (BST) Menggunakan Python

## Deskripsi Singkat
Program ini merupakan implementasi struktur data Binary Search Tree (BST) menggunakan bahasa pemrograman Python. BST adalah struktur data berbentuk pohon (tree) yang digunakan untuk menyimpan data secara terurut sehingga proses pencarian, penambahan, dan traversal data dapat dilakukan dengan lebih efisien. Pada program ini, pengguna dapat melakukan beberapa operasi seperti menambahkan data (insert), mencari data (search), serta menampilkan data menggunakan traversal inorder.

## Source Code
<img width="974" height="836" alt="image" src="https://github.com/user-attachments/assets/5a3856f7-a1f6-473c-b74d-da3ec564327f" />
<img width="873" height="734" alt="image" src="https://github.com/user-attachments/assets/50cdbcdb-2ab2-42e1-a59b-5de0e5dd76f6" />
<img width="862" height="796" alt="image" src="https://github.com/user-attachments/assets/cfbd096a-2bf8-4d9d-85ef-ca264b2c8f15" />

Penjelasan Source Code

class Node:
- Membuat class Node untuk merepresentasikan node pada Binary Search Tree.

def __init__(self, data):
- Method constructor untuk menginisialisasi objek node.

self.data = data
- Menyimpan nilai/data pada node.

self.left = None
- Membuat pointer anak kiri dengan nilai awal None.

self.right = None
- Membuat pointer anak kanan dengan nilai awal None.

class BST:
- Membuat class BST untuk mengelola Binary Search Tree.

def __init__(self):
- Constructor class BST.

self.root = None
- Menentukan root awal tree kosong (None).

def insert(self, root, data):
- Method untuk menambahkan data ke BST.

if root is None:
- Mengecek apakah node kosong.

 return Node(data)
 - Jika kosong, buat node baru.

if data < root.data:
- Mengecek apakah data lebih kecil dari root.

root.left = self.insert(root.left, data)
- Jika lebih kecil, data dimasukkan ke subtree kiri.

root.right = self.insert(root.right, data)
- Data dimasukkan ke subtree kanan.

return root
- Mengembalikan node root.

def inorder(self, root):
- Method traversal inorder.

if root:
- Mengecek apakah node ada.

self.inorder(root.left)
- Mengunjungi subtree kiri.

print(root.data, end=" ")
- Menampilkan data node.

self.inorder(root.right)
- Mengunjungi subtree kanan.

def search(self, root, key):
- Method untuk mencari data pada BST.

if root is None:
- Jika node kosong.

return False
- Data tidak ditemukan.

if root.data == key:
- Mengecek apakah data sama dengan key.

return True
- Jika sama, data ditemukan.

if key < root.data:
- Jika key lebih kecil dari root.

return self.search(root.left, key)
- Cari ke subtree kiri.

return self.search(root.right, key)
- Jika lebih besar, cari ke subtree kanan.

print("\n=== MENU BST ===")
- Menampilkan judul menu.

print("1. Insert")
- Menu menambah data.

print("2. Search")
- Menu mencari data.

print("3. Inorder")
- Menu traversal inorder.

print("4. Keluar")
- Menu keluar program.

pilih = int(input("Pilih menu: "))
- Meminta input pilihan menu dari pengguna.

if pilih == 1:
- Jika pengguna memilih menu insert.

data = int(input("Masukkan data: "))
- Meminta data yang akan dimasukkan.

bst.root = bst.insert(bst.root, data)
- Menambahkan data ke BST.

elif pilih == 2:
- Jika memilih menu search.

key = int(input("Cari data: "))
- Meminta data yang ingin dicari.

if bst.search(bst.root, key):
- Mengecek apakah data ditemukan.

print("Data ditemukan")
- Menampilkan pesan jika data ada.

elif pilih == 3:
- Jika memilih menu inorder.

print("Inorder: ", end="")
- Menampilkan tulisan “Inorder”.

bst.inorder(bst.root)
- Menjalankan traversal inorder.

elif pilih == 4:
- Jika memilih menu keluar.

if __name__ == "__main__":
main()
- Untuk menjalankan fungsi

## Output Program
<img width="779" height="882" alt="image" src="https://github.com/user-attachments/assets/396e96da-380c-4617-b6b5-378975ba04fc" />

Penjelasan Output Program

Program menampilkan daftar menu yang dapat dipilih pengguna, yaitu:
- Insert → menambahkan data ke BST
- Search → mencari data dalam BST
- Inorder → menampilkan isi BST secara terurut
- Keluar → menghentikan program

User memilih menu 1 (Insert) lalu memasukkan nilai 2.
Program kemudian:

- membuat node baru bernilai 2
- menjadikannya sebagai root karena BST masih kosong

User memilih menu 2 (Search) dan mencari nilai 2.

Program melakukan pencarian:

- mengecek root
- root bernilai 2

User memilih menu 3 (Inorder).

Traversal inorder memiliki urutan:

- Kiri
- Root
- Kanan

User memilih menu 4 (Keluar).

## Link Youtube
https://youtu.be/UTZh4WhHu0w














