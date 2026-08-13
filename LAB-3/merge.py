def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l=arr[:mid]
    r=arr[mid:]

    merge(l)
    merge(r)

    i=j=k=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            arr[k]=l[i]
            i+=1
        elif r[j]<l[i]:
            arr[k]=r[j]
            j+=1
        k+=1
    while i<len(l):
        arr[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        arr[k]=r[j]
        j+=1
        k+=1
    return arr
        
a=input("Enter Elelments in Array : ")
arr=list(map(int,a.split()))
print("Unsorted Array : ",arr)
print("Sorted array : ",merge(arr))
