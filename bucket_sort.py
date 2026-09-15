def bucketSort(L, N): 
    B = [[] for _ in range(N)]

    while L:
        k, o = L.pop(0)
        B[k].append((k, o))

    for i in range(N):
        while B[i]:
            k, o = B[i].pop(0)  
            L.append((k, o)) 

    
ar=[5,2,8,9,5,8,3,7,4,6]
L = [(3, 'e'), (1, 'b'), (2, 'c'), (0, 'd'), (3, 'a'), (2, 'f')]
N = 4 
bucketSort(L, N)
print(L)