def selection(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

a=input("Enter Elelments in Array : ")
arr=list(map(int,a.split()))
print("Unsorted Array : ",arr)
print("Sorted array : ",selection(arr))
