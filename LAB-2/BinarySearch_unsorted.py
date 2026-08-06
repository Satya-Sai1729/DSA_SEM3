def search(l,h,target,arr):
    while l<=h:
        m=(l+h)//2
        if arr[m]==target:
            return m
        elif arr[m]<target:
            l=m+1
        else:
            h=m-1
    return -1

n=int(input("Enter no of employees : "))
arr=[]
for i in range(n):
    a=int(input(f"Enter ID of {i+1} Employee : "))
    arr.append(a)
print()
arr.sort()
target=int(input("Enter Element to be searched : "))
s=search(0,len(arr)-1,target,arr)
if s==-1:
    print("Element not found")
else:
    print("Element found at ",s)
