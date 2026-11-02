SIZE = 10

# Separate Chaining
chain = [[] for _ in range(SIZE)]

# Linear Probing
linear = [None] * SIZE

# Quadratic Probing
quadratic = [None] * SIZE


# Hash function
def hash_func(key):
    return key % SIZE


# Separate Chaining
def chaining(key):
    index = hash_func(key)
    if key not in chain[index]:
        chain[index].append(key)
        print("Inserted successfully.")
    else:
        print("Duplicate key!")


# Linear Probing
def linear_probing(key):
    index = hash_func(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if linear[pos] == key:
            print("Duplicate key!")
            return

        if linear[pos] is None:
            linear[pos] = key
            print("Inserted successfully.")
            return

    print("Hash table is full.")


# Quadratic Probing
def quadratic_probing(key):
    index = hash_func(key)

    for i in range(SIZE):
        pos = (index + i * i) % SIZE

        if quadratic[pos] == key:
            print("Duplicate key!")
            return

        if quadratic[pos] is None:
            quadratic[pos] = key
            print("Inserted successfully.")
            return

    print("No empty position found.")


# Search
def search(table, key, method):
    index = hash_func(key)

    if method == 1:  # Chaining
        return key in table[index]

    for i in range(SIZE):
        if method == 2:
            pos = (index + i) % SIZE
        else:
            pos = (index + i * i) % SIZE

        if table[pos] is None:
            return False

        if table[pos] == key:
            return True

    return False


# Display
def display(table, method):
    for i in range(SIZE):
        print(i, ":", table[i])


# Main program
while True:
    print("\n----- HASHING -----")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Exiting program.")
        break

    if choice not in [1, 2, 3]:
        print("Invalid choice!")
        continue

    table = [chain, linear, quadratic][choice - 1]

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Back to Main Menu")

        op = int(input("Enter operation: "))

        if op == 1:
            key = int(input("Enter key: "))

            if choice == 1:
                chaining(key)
            elif choice == 2:
                linear_probing(key)
            else:
                quadratic_probing(key)

        elif op == 2:
            key = int(input("Enter key: "))
            print("Key found." if search(table, key, choice)
                  else "Key not found.")

        elif op == 3:
            display(table, choice)

        elif op == 4:
            break

        else:
            print("Invalid operation!")
