def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    equal = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quick_sort(left) + equal + quick_sort(right)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    sorted_array = quick_sort(array)
    print("Sorted array:", sorted_array)