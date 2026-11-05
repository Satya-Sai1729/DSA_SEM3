class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # 1. INSERTION
    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)

        elif value > root.data:
            root.right = self.insert(root.right, value)

        else:
            print("Duplicate value not allowed")

        return root

    # 2. SEARCHING
    def search(self, root, key):

        if root is None:
            return False

        if root.data == key:
            return True

        elif key < root.data:
            return self.search(root.left, key)

        else:
            return self.search(root.right, key)

    # 3. INORDER (LEFT ROOT RIGHT)
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # 4. PREORDER (ROOT LEFT RIGHT)
    def preorder(self, root):

        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # 5. POSTORDER (LEFT RIGHT ROOT)
    def postorder(self, root):

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # 6. FIND MINIMUM VALUE
    def find_min(self, root):

        while root.left is not None:
            root = root.left

        return root

    # 7. DELETION
    def delete(self, root, key):

        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:

            # CASE 1: NO CHILDREN
            if root.left is None and root.right is None:
                return None

            # CASE 2: ONLY RIGHT CHILD
            elif root.left is None:
                return root.right

            # CASE 2: ONLY LEFT CHILD
            elif root.right is None:
                return root.left

            # CASE 3: TWO CHILDREN
            else:
                temp = self.find_min(root.right)

                root.data = temp.data

                root.right = self.delete(root.right, temp.data)

        return root


# MAIN PROGRAM

b = BST()

while True:

    print("\n--- BINARY SEARCH TREE ---")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder")
    print("4. Preorder")
    print("5. Postorder")
    print("6. Delete")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        value = int(input("Enter value: "))
        b.root = b.insert(b.root, value)

    elif ch == 2:
        key = int(input("Enter value to search: "))

        if b.search(b.root, key):
            print("Element found")
        else:
            print("Element not found")

    elif ch == 3:
        print("Inorder traversal:")
        b.inorder(b.root)
        print()

    elif ch == 4:
        print("Preorder traversal:")
        b.preorder(b.root)
        print()

    elif ch == 5:
        print("Postorder traversal:")
        b.postorder(b.root)
        print()

    elif ch == 6:
        key = int(input("Enter value to delete: "))
        b.root = b.delete(b.root, key)
        print("Deletion operation completed")

    elif ch == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
