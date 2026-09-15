def insertion_sort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i 

        while j > 0 and arr[j - 1] > element:
            arr[j] = arr[j - 1]
            j = j - 1

        arr[j] = element 
    return arr

arr=[5,3,7,2,1,5,8]
print(insertion_sort(arr))