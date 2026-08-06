def search(target,arr,i):
    if i<len(arr):
        if target==arr[i]:
            return i
        else:
            return search(target,arr,i+1)
    return -1

n=int(input("Enter no of employees : "))
arr=[]
for i in range(n):
    a=int(input(f"Enter ID of {i+1} Employee : "))
    arr.append(a)
print()
arr.sort()
target=int(input("Enter empoyee ID to be searched : "))
s=search(target,arr,0)
if s==-1:
    print("Employee ID not found")
else:
    print("Employee ID found at ",s)

"""
ALternative Method:
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
"""
