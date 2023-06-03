import sys

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

def findcost(visited, g):
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

    return totCost

if __name__ == '__main__':
    
    g = Graph(7)
    g.addEdge(0, 1, 1)
    g.addEdge(0, 2, 20)
    g.addEdge(0, 3, 50)
    g.addEdge(0, 4, 50)
    g.addEdge(0, 5, 50)
    g.addEdge(0, 6, 2533)
    g.addEdge(1, 2, 345)
    g.addEdge(1, 3, 20)
    g.addEdge(1, 4, 50)
    g.addEdge(1, 5, 50)
    g.addEdge(1, 6, 50)
    g.addEdge(2, 3, 433)
    g.addEdge(2, 4, 20)
    g.addEdge(2, 5, 50)
    g.addEdge(2, 6, 50)
    g.addEdge(3, 4, 334)
    g.addEdge(3, 5, 20)
    g.addEdge(3, 6, 50)
    g.addEdge(4, 5, 434)
    g.addEdge(4, 6, 20)
    g.addEdge(5, 6, 20)

    start = 0
    paths = dict()
    totCost = 0
    flag = False

    paths[str(start)] = 0

    while(1):
        mincost = min(paths.values())
        path = [key for key in paths if paths[key] == mincost][0]
        prefix = path + '-'
        del paths[path]

        visited = []
        for node in path.split('-'):     
            visited.append(int(node))

        root = visited[len(visited)-1]
        rootcost = findcost(visited, g)

        if flag and root==start:
            print('Final Path Chosen: ', visited)
            print('Cost: ', findcost(visited, g))
            exit(0)

        if len(visited)==g.V:
            flag = True
            visited.pop(0)
        
        for edge in g.graph:
            if (edge[0]==root and edge[1] not in visited) or (edge[0] not in visited and edge[1]==root):
                
                if edge[0]==root:
                    visited.append(edge[1])
                else:
                    visited.append(edge[0])

                edgeslist = []
                verticelist = []

                for cedge in g.graph:
                    if cedge[0] not in visited and cedge[1] not in visited:
                        edgeslist.append(cedge)
                        
                        if cedge[0] not in verticelist:
                            verticelist.append(cedge[0])
                        
                        if cedge[1] not in verticelist:
                            verticelist.append(cedge[1])
                
                visited.pop()
                verticelist.sort()
                temp = Graph(len(verticelist))

                for newedge in edgeslist:
                    temp.addEdge(verticelist.index(newedge[0]), verticelist.index(newedge[1]), newedge[2])

                cost = rootcost + temp.KruskalMST() + edge[2]

                if edge[0]==root:
                    paths[prefix + str(edge[1])] = cost
                else:
                    paths[prefix + str(edge[0])] = cost
