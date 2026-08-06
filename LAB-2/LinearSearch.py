def search(target,arr):
    i=0
    while i<len(arr):
        if arr[i]==target:
            return i
        i+=1
    return -1

a=input("Enter Elelments in Array : ")
arr=[int(i) for i in a.split()]

target=int(input("Enter Element to be searched : "))
s=search(target,arr)
if s==-1:
    print("Element not found")
else:
    print("Element found at index : ",s)

