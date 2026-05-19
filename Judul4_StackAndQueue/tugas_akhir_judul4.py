class Stack:
    def __init__(self, ukuran=10):
        self.data = [0] * ukuran
        self.top = -1
        self.ukuran = ukuran

    def push(self, nilai):
        if self.top == self.ukuran - 1:
            print("Stack penuh")
        else:
            self.top += 1
            self.data[self.top] = nilai
            print(f"{nilai} ditambahkan")

    def pop(self):
        if self.top == -1:
            print("Stack kosong")
        else:
            print(f"{self.data[self.top]} dihapus")
            self.top -= 1

    def tampil(self):
        if self.top == -1:
            print("Stack kosong")
        else:
            print("Isi stack:", end=" ")
            for i in range(self.top, -1, -1):
                print(self.data[i], end=" ")
            print()


def main():
    s = Stack()

    while True:
        print("\n=== MENU STACK ===")
        print("1. Push")
        print("2. Pop")
        print("3. Tampil")
        print("4. Keluar")

        pilih = int(input("Pilih: "))

        if pilih == 1:
            nilai = int(input("Masukkan nilai: "))
            s.push(nilai)

        elif pilih == 2:
            s.pop()

        elif pilih == 3:
            s.tampil()

        elif pilih == 4:
            print("Program selesai")
            break

        else:
            print("Pilihan salah")


if __name__ == "__main__":
    main()