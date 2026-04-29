class Node:
    def __init__(self, pembelian):
        self.pembelian = pembelian
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_pembelian(self, pembelian):
        new_node = Node(pembelian)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print(f"Pembelian '{pembelian}' ditambahkan.")

    def tampilkan_pembelian(self):
        if self.head is None:
            print("Tidak ada pembelian.")
            return

        print("\nDaftar Pembelian:")
        temp = self.head
        no = 1
        while temp:
            print(f"{no}. {temp.pembelian}")
            temp = temp.next
            no += 1

    def proses_pembelian(self):
        if self.head is None:
            print("Belum ada pembelian.")
        else:
            print(f"Pembelian '{self.head.pembelian}' diproses.")
            self.head = self.head.next


def menu():
    print("\n=== Sistem Pembelian Buku ===")
    print("1. Tambah pembelian")
    print("2. Tampilkan pembelian")
    print("3. Proses pembelian")
    print("4. Keluar")


def main():
    daftar = LinkedList()

    while True:
        menu()
        try:
            pilihan = int(input("Pilih Buku: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == 1:
            pembelian = input("Masukkan nama buku: ")
            daftar.tambah_pembelian(pembelian)

        elif pilihan == 2:
            daftar.tampilkan_pembelian()

        elif pilihan == 3:
            daftar.proses_pembelian()
            
        elif pilihan == 4:
            print("program selesai.")
            break

        else:
            print("Pembelian tidak valid!")


if __name__ == "__main__":
    main()