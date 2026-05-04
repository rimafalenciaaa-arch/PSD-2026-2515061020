def insertion_sort(jumlah, n):
    for i in range(1, n):
        temp = jumlah[i]
        j = i - 1
        while j >= 0 and jumlah[j] < temp:
            jumlah[j + 1] = jumlah[j]
            j -= 1
        jumlah[j + 1] = temp


def main():
    try: 
        n = int(input("Masukkan jumlah makanan: "))
    except ValueError:
        print("Input tidak valid!")
        return
    jumlah = []
    print("Masukkan daftar harga makanan:")
    for i in range(n):
        while True:
            try:
                nilai = int(input())
                jumlah.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Harga sebelum diurutkan: {jumlah}")
    insertion_sort(jumlah, n)
    print("Harga setelah diurutkan (Insertion Sort):", end=" ")
    for i in range(n):
        print(jumlah[i], end=" ")
    print()


if __name__ == "__main__":
    main()