def ShellSort(arr):
    maxGap=(len(arr)-1)//3
    h=1
    while h<=maxGap:
        h=h*3+1
    while 0<h:
        segmentInsertionSort(arr, int(h))
        h=(h-1)/3
    return arr

def segmentInsertionSort(arr, gap):
    for i in range(gap, len(arr)):
        j=i
        insert_elem=arr[i]
        while j>gap-1 and insert_elem<arr[j-gap]:
            arr[j]=arr[j-gap]
            j=j-gap
        arr[j]=insert_elem
        
arr=[4,5,8,1,2,9,3,7,14,5]
sorted=ShellSort(arr)
print(sorted)