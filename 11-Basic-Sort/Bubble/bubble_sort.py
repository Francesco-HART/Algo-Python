def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([4,2,6,5,1,3]))

print("""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """)
 

 
 