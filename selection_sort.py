def SelectionSort(arr):
    for i in range(len(arr)-1):
        min=arr[i]
        minIndex=i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        if i != min_index:
            swap_elements(arr, i, min_index)

def swap_elements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
arr = [64, 25, 12, 22, 11]
SelectionSort(arr)
print("Sorted array:", arr)