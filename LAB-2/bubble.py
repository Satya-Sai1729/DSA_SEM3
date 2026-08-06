def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

a=input("Enter Elelments in Array : ")
arr=[int(i) for i in a.split()]
print("Unsorted Array : ",arr)
print("Sorted array : ",bubble(arr))
