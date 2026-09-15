import heapq

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            self.parent[root2] = root1  

def kruskal_with_heapq(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            if (neighbor, node, weight) not in edges:
                heapq.heappush(edges, (weight, node, neighbor))

    dsu = DisjointSet(graph.keys())

    mst = []  
    total_weight = 0

    while edges and len(mst) < len(graph) - 1:
        weight, u, v = heapq.heappop(edges)
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


graph = {
    'A': [('B', 2), ('C', 8),('E',7)],
    'B': [('A', 2), ('C', 5), ('D', 7)],
    'C': [('A', 8), ('B', 5), ('D', 9),('E',8)],
    'D': [('B', 7), ('C', 9),('F',4)],
    'E': [('A', 7), ('C', 8),('F',3)],
    'F': [('D', 4), ('E', 3)]
}
mst, total_weight = kruskal_with_heapq(graph)
print("Edges in the MST:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
print(f"Total weight of MST: {total_weight}")