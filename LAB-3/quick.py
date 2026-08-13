def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)

a=input("Enter Elelments in Array : ")
arr=list(map(int,a.split()))
print("Unsorted Array : ",arr)
print("Sorted array : ",quick_sort(arr))
