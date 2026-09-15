def BubbleSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-2):
            if arr[j]>arr[j+1]:
                swapElements(arr, j, j+1)
    return arr

def swapElements(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    
arr=[4,3,7,1,2,9]
sorted=BubbleSort(arr)
print(sorted)