class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert data
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Search data
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right)


def main():
    bst = BST()

    while True:
        print("\n=== MENU BST ===")
        print("1. Insert")
        print("2. Search")
        print("3. Inorder")
        print("4. Keluar")

        pilih = int(input("Pilih menu: "))

        if pilih == 1:
            data = int(input("Masukkan data: "))
            bst.root = bst.insert(bst.root, data)

        elif pilih == 2:
            key = int(input("Cari data: "))

            if bst.search(bst.root, key):
                print("Data ditemukan")
            else:
                print("Data tidak ditemukan")

        elif pilih == 3:
            print("Inorder: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Program selesai")
            break

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()