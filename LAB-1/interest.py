def intrest(p,n):
    if n==0:
        return 1
    return p*intrest(p,n-1)
p=int(input("Enter Principal amount : "))
n=float(input("Enter no of years : "))
print("The simple intrest is ",intrest(p,n))
