def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        replaced = False

        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                replaced = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not replaced:
            break
        
arr = list(map(float,input().split()))
bubble_sort(arr)
print("Sorted array is:", arr)
