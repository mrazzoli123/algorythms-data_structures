from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")
            
    def dfs(self, start, visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor,visited)
                
    def bfs(self, start):
        visited=set()
        queue=deque([start])
        while queue:
            vertex=queue.popleft()
            if vertex not in visited:
                print(vertex,end='  ')
                visited.add(vertex)
                
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                    
                        
if __name__=="__main__":
    g=Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print("Graph Representation:")
    g.print_graph()
    print("DFS starting from vertex 2:")
    g.dfs(2)
    print("\nBFS starting from vertex 2:")
    g.bfs(2)
    
    