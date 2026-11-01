class AVLTree:
    def __init__(self):
        self.keys = []
        self.left = []
        self.right = []
        self.height = []
        self.root = -1

    # Create a new node
    def create_node(self, key):
        i = len(self.keys)
        self.keys.append(key)
        self.left.append(-1)
        self.right.append(-1)
        self.height.append(1)
        return i

    # Get height and balance factor
    def get_height(self, i):
        return 0 if i == -1 else self.height[i]

    def balance(self, i):
        if i == -1:
            return 0
        return self.get_height(self.left[i]) - self.get_height(self.right[i])

    # Update height
    def update_height(self, i):
        self.height[i] = 1 + max(
            self.get_height(self.left[i]),
            self.get_height(self.right[i])
        )

    # Right rotation
    def right_rotate(self, y):
        x = self.left[y]
        t2 = self.right[x]

        self.right[x] = y
        self.left[y] = t2

        self.update_height(y)
        self.update_height(x)
        return x

    # Left rotation
    def left_rotate(self, x):
        y = self.right[x]
        t2 = self.left[y]

        self.left[y] = x
        self.right[x] = t2

        self.update_height(x)
        self.update_height(y)
        return y

    # Balance the tree
    def rebalance(self, i, key=None):
        self.update_height(i)
        bf = self.balance(i)

        # LL case
        if bf > 1 and self.balance(self.left[i]) >= 0:
            return self.right_rotate(i)

        # RR case
        if bf < -1 and self.balance(self.right[i]) <= 0:
            return self.left_rotate(i)

        # LR case
        if bf > 1 and self.balance(self.left[i]) < 0:
            self.left[i] = self.left_rotate(self.left[i])
            return self.right_rotate(i)

        # RL case
        if bf < -1 and self.balance(self.right[i]) > 0:
            self.right[i] = self.right_rotate(self.right[i])
            return self.left_rotate(i)

        return i

    # Insert
    def insert_node(self, i, key):
        if i == -1:
            return self.create_node(key)

        if key < self.keys[i]:
            self.left[i] = self.insert_node(self.left[i], key)
        elif key > self.keys[i]:
            self.right[i] = self.insert_node(self.right[i], key)
        else:
            print("Duplicate values are not allowed")
            return i

        return self.rebalance(i)

    # Search
    def search(self, i, key):
        if i == -1:
            return False

        if self.keys[i] == key:
            return True

        if key < self.keys[i]:
            return self.search(self.left[i], key)

        return self.search(self.right[i], key)

    # Find minimum node
    def min_node(self, i):
        while self.left[i] != -1:
            i = self.left[i]
        return i

    # Delete
    def delete_node(self, i, key):
        if i == -1:
            return -1

        if key < self.keys[i]:
            self.left[i] = self.delete_node(self.left[i], key)

        elif key > self.keys[i]:
            self.right[i] = self.delete_node(self.right[i], key)

        else:
            # No left child
            if self.left[i] == -1:
                return self.right[i]

            # No right child
            if self.right[i] == -1:
                return self.left[i]

            # Two children
            temp = self.min_node(self.right[i])
            self.keys[i] = self.keys[temp]
            self.right[i] = self.delete_node(
                self.right[i], self.keys[temp]
            )

        return self.rebalance(i)

    # Inorder traversal
    def inorder(self, i):
        if i != -1:
            self.inorder(self.left[i])
            print(self.keys[i], end=" ")
            self.inorder(self.right[i])

    # Preorder traversal
    def preorder(self, i):
        if i != -1:
            print(self.keys[i], end=" ")
            self.preorder(self.left[i])
            self.preorder(self.right[i])

    # Postorder traversal
    def postorder(self, i):
        if i != -1:
            self.postorder(self.left[i])
            self.postorder(self.right[i])
            print(self.keys[i], end=" ")

    # Display tree
    def display(self, i, level=0):
        if i != -1:
            self.display(self.right[i], level + 1)
            print("   " * level + str(self.keys[i]))
            self.display(self.left[i], level + 1)


# Main program
avl = AVLTree()

while True:
    print("\n----- AVL TREE USING ARRAYS -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display Tree")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            avl.root = avl.insert_node(avl.root, key)
            print("Insertion completed.")

        elif choice == 2:
            key = int(input("Enter value to delete: "))

            if avl.search(avl.root, key):
                avl.root = avl.delete_node(avl.root, key)
                print("Node deleted successfully.")
            else:
                print("Value not found.")

        elif choice == 3:
            key = int(input("Enter value to search: "))
            print("Value found." if avl.search(avl.root, key)
                  else "Value not found.")

        elif choice == 4:
            print("Inorder:", end=" ")
            avl.inorder(avl.root)
            print()

        elif choice == 5:
            print("Preorder:", end=" ")
            avl.preorder(avl.root)
            print()

        elif choice == 6:
            print("Postorder:", end=" ")
            avl.postorder(avl.root)
            print()

        elif choice == 7:
            if avl.root == -1:
                print("Tree is empty.")
            else:
                avl.display(avl.root)

        elif choice == 8:
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid integer.")
