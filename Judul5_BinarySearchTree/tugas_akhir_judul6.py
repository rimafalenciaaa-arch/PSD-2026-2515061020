class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def display(self):
        print("\nIsi Hash Map:")
        for i in range(self.size):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    hm = HashMap()

    hm.insert(1, "Andre")
    hm.insert(6, "Tio")
    hm.insert(11, "Rani")

    hm.display()

    key = int(input("\nCari key: "))
    hasil = hm.search(key)

    if hasil:
        print("Data ditemukan:", hasil)
    else:
        print("Data tidak ditemukan")


if __name__ == "__main__":
    main()