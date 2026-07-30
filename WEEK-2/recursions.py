def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def sum1(n):
    if n==0:
        return 0
    return n+sum(n-1)
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-1)
print(f"1.Factorial of n\n2.Sum of n integers\n3.Fibonacci(n)")
n=int(input("Enter the value : "))
c=int(input("Enter your choice : "))

while True:
    if c==1:
        print("Factorial of the Number : ",fact(n))
    elif c==2:
        print("Sum of n integers is : ",sum1(n))
    elif c==3:
        print(n,"th number of Fibonacci series : ",fibo(n))
    else:
        print("Enter Valid choice")
    c=int(input("Enter your choice : "))
    if c==4:
        print("Thank you")
        break
