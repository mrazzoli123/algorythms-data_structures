import heapq

def prim(graph, start):

    priority_queue = []
    for neighbor, weight in graph[start]:
        heapq.heappush(priority_queue, (weight, start, neighbor))

    visited = set()
    visited.add(start)

    mst = []
    total_weight = 0

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)

        if v in visited:
            continue

        mst.append((u, v, weight))
        total_weight += weight
        visited.add(v)

        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (w, v, neighbor))

    return mst, total_weight

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}
start_node = 'A'
mst, total_weight = prim(graph, start_node)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} (weight: {weight})")
print(f"\nTotal weight of the MST: {total_weight}")
