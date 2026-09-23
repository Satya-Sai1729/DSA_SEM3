class Stack_Array:
    def __init__(self, length):
        self.length = length
        self.stack = []
        self.top = -1

    def stack_push(self, data):
        if len(self.stack) == self.length:
            print("Stack is full")
            return

        self.stack.append(data)
        self.top += 1
        print("Element pushed successfully")

    def stack_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print(self.stack.pop(), "removed")
        self.top -= 1

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def top_index(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element index:", self.top)

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])

    def count(self):
        print("Number of elements:", len(self.stack))


s = Stack_Array(5)

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Count")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element: "))
        s.stack_push(data)

    elif choice == 2:
        s.stack_pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        s.count()

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
