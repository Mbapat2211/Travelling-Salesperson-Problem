import sys
import random

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def KruskalMST(self):
 
        result = [] 
        i = 0
        e = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
 
        parent = []
        rank = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        
        for u, v, weight in result:
            minimumCost += weight
        
        return minimumCost

if __name__ == '__main__':
    
    g = Graph(50)
    for i in range(49):
        for j in range(i+1, 50):
            g.addEdge(i, j, random.randint(1,10))
    
    visited = []
    root = 0
    visited.append(root)
    totCost = 0
    
    while len(visited) < g.V:
        
        minimum = sys.maxsize
        
        for edge in g.graph:
            
            if (edge[0]==root and edge[1] not in visited) or (edge[0] not in visited and edge[1]==root):
                
                temp = Graph(g.V - len(visited))
                
                edgeslist = []
                verticelist = []

                for cedge in g.graph:
                    
                    if cedge[0] not in visited and cedge[1] not in visited:
                        
                        edgeslist.append(cedge)
                        
                        if cedge[0] not in verticelist:
                            verticelist.append(cedge[0])
                        
                        if cedge[1] not in verticelist:
                            verticelist.append(cedge[1])
                
                verticelist.sort()
                
                for newedge in edgeslist:
                    temp.addEdge(verticelist.index(newedge[0]), verticelist.index(newedge[1]), newedge[2])
                    
                cost = edge[2] + temp.KruskalMST()
                
                if cost<minimum:
                    
                    minimum = cost

                    if edge[0]==root:
                        newvertex = edge[1]
                    
                    else:
                        newvertex = edge[0]
        
        root = newvertex
        visited.append(root)

    visited.append(visited[0])
    
    i = 1
    totCost = 0
    
    while i<len(visited):
        
        for edge in g.graph:
            
            if visited[i]>visited[i-1]:
                
                if edge[0]==visited[i-1] and edge[1]==visited[i]:
                    totCost = totCost + edge[2]
            
            else:
                
                if edge[1]==visited[i-1] and edge[0]==visited[i]:
                    totCost = totCost + edge[2]    
        
        i = i + 1
    
    print('Final Path Choosen: ', visited)
    print('Cost: ', totCost)