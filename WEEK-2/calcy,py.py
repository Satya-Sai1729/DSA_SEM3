def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by zero is invalid"
def mul(a,b):
    return a*b
print(f"Welcome to basic calculator : \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n")
while True:
    a=int(input("Enter the value of integer 1 : "))
    b=int(input("Enter the value of integer 2 : "))    

    c=int(input("Enter the choice between 1 to 4 : "))

    if c==1:
        print("Sum : ",add(a,b))
    elif c==2:
        print("Difference : ",sub(a,b))
    elif c==3:
        print("Product : ",mul(a,b))
    elif c==4:
        print("Result : ",div(a,b))
    else:
        print("Invalid Choice")
    print()

    again=input("Do you want to Try again (y/n)? :")
    print()

    if again.lower() != "y":
        print("Thank You")
        break
    
