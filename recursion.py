def countdown(n):
    if n <= 0:
        print("Liftoff!")
    else:
        print(n)
        return countdown(n - 1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def recursive_linear_search(arr, target, index=0):
    if index >= len(arr):
        return -1

    if arr[index] == target:
        return index

    return recursive_linear_search(arr, target, index + 1)

def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, high)
    
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1