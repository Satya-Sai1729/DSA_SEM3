class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter value: "))
            self.insert_end(data)
        print("Linked list created.")

    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
            new.next = new
        else:
            new.next = self.head
            self.head = new
            self.tail.next = self.head

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
            new.next = new
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

    def insert_index(self, data, index):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_begin(data)
            return

        temp = self.head
        for i in range(index - 1):
            if temp == self.tail:
                print("Invalid index.")
                return
            temp = temp.next

        if temp == self.tail:
            if index == self.count():
                self.insert_end(data)
            else:
                print("Invalid index.")
            return

        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete_value(self, key):
        if self.head is None:
            print("List is empty.")
            return

        curr = self.head
        prev = self.tail

        while True:
            if curr.data == key:
                if curr == self.head:
                    self.delete_begin()
                elif curr == self.tail:
                    self.delete_end()
                else:
                    prev.next = curr.next
                    print("Node deleted.")
                return

            prev = curr
            curr = curr.next

            if curr == self.head:
                break

        print("Value not found.")

    def delete_begin(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        print("Beginning node deleted.")

    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next

            self.tail = temp
            self.tail.next = self.head

        print("Last node deleted.")

    def count(self):
        if self.head is None:
            return 0

        count = 1
        temp = self.head

        while temp.next != self.head:
            count += 1
            temp = temp.next

        return count

    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(Head)")

    def show_head_tail(self):
        if self.head is None:
            print("List is empty.")
        else:
            print("Head:", self.head.data)
            print("Tail:", self.tail.data)


cll = CircularLinkedList()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete at Beginning")
    print("7. Delete at End")
    print("8. Count Nodes")
    print("9. Display / Traverse")
    print("10. Display Head and Tail")
    print("11. Exit")

    try:
        ch = int(input("Enter your choice: "))

        if ch == 1:
            if cll.head is not None:
                print("List already exists.")
            else:
                cll.create()

        elif ch == 2:
            data = int(input("Enter value: "))
            cll.insert_begin(data)

        elif ch == 3:
            data = int(input("Enter value: "))
            cll.insert_end(data)

        elif ch == 4:
            data = int(input("Enter value: "))
            index = int(input("Enter index: "))
            cll.insert_index(data, index)

        elif ch == 5:
            key = int(input("Enter value to delete: "))
            cll.delete_value(key)

        elif ch == 6:
            cll.delete_begin()

        elif ch == 7:
            cll.delete_end()

        elif ch == 8:
            print("Number of nodes:", cll.count())

        elif ch == 9:
            cll.display()

        elif ch == 10:
            cll.show_head_tail()

        elif ch == 11:
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid integer.")

