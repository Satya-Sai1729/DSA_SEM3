n=int(input("Enter the length of the Pattern : "))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

print()

for i in range(n):
    for j in range(n-i,0,-1):
        print("*",end="")
    print()

print()

for i in range(n):
    for j in range(1,i+2):
        print(j,end="")
    print()

print()

k=1
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*k,end="")
    k+=2
    print()

print()

for i in range(n):
    for j in range(0,i+1):
        print(chr(65+j),end="")
    print()

print()





