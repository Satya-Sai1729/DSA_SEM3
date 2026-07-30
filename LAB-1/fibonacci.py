def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
a=int(input("Enter a Number : "))
for i in range(a):
    print(fibo(i),end=" ")
print()
print(f"The {a}th element of Fibonacci series is ",fibo(a-1))
