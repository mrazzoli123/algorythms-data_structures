import heapq

def prim_jarnik_mst(graph):
    
    pq = []
    vertex_info = {}
    for vertex in graph.keys():
        vertex_info[vertex] = [float('inf'), None]
        heapq.heappush(pq, (float('inf'), vertex))
        
    start = next(iter(graph))
    vertex_info[start][0] = 0
    heapq.heappush(pq, (0, start))

    mst = []
    total_weight = 0
    in_mst = set()

    while pq:
        key, u = heapq.heappop(pq)
        if u in in_mst:
            continue
        in_mst.add(u)
        if vertex_info[u][1] is not None:
            mst.append(vertex_info[u][1])
            total_weight += key

        for v, weight in graph[u]:
            if v not in in_mst and weight < vertex_info[v][0]:
                vertex_info[v] = [weight, (u, v, weight)] 
                heapq.heappush(pq, (weight, v))

    return mst, total_weight

graph = {
    'A': [('B', 2), ('C', 8),('E',7)],
    'B': [('A', 2), ('C', 5), ('D', 7)],
    'C': [('A', 8), ('B', 5), ('D', 9),('E',8)],
    'D': [('B', 7), ('C', 9),('F',4)],
    'E': [('A', 7), ('C', 8),('F',3)],
    'F': [('D', 4), ('E', 3)]
}
mst, total_weight = prim_jarnik_mst(graph)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} (weight: {weight})")
print(f"\nTotal weight of the MST: {total_weight}")