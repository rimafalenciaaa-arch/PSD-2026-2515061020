def binary_search(arr, target):
    l = 0
    r = 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari nilai di kanan")
            l = m + 1
        else:
            print("Mencari nilai di kiri")
            r = m - 1
    return pos


def main():
    try:
        n = int(input("Masukkan jumlah nilai: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan nilai (urut menurun):")
    for i in range(n):
        while True:
            try:
                nilai = int(input())
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Array: {arr}")
    while True:
        try:
            target = int(input("Masukkan angka yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    pos = binary_search(arr, target)
    if pos != -1:
        print(f"Ditemukan pada indeks ke-{pos}")
    else:
        print("Tidak ditemukan")


if __name__ == "__main__":
    main()