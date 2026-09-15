def heapsort(arr):
    buildHeap(arr)
    end=len(arr)-1
    while end>0:
        swapElements(arr,0,end)
        end-=1
        downHeap(arr,0,end)
    return arr

def buildHeap(arr):
    last=len(arr)-1
    next=last
    while next > 0:
        downHeap(arr, parent(next), last)
        next=next-2
    
def parent(i):
    return (i-1) // 2

def downHeap(H, i, last):
    property=False
    while property==False:
        maxIndex= indexOfMax(H, i, last)
        if maxIndex!=i:
            swapElements(H, maxIndex, i)
            i=maxIndex
        else:
            property=True

def swapElements(H,j,k):
    temp=H[j]
    H[j]=H[k]
    H[k]=temp
    
def indexOfMax(A,r,last):
    largest=r
    left=2*r+1
    right=left+1
    if left <=last and A[left]>A[largest]:
        largest=left
    if right <=last and A[right]>A[largest]:
        largest=right
    return largest

arr=[8,7,3,11,6,2,5]
print(heapsort(arr))