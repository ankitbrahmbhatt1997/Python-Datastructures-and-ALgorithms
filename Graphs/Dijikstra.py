from heapq import heappush,heappop,heapify

class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.distance = None

    def addNeighbour(self,nbr,cost=0):
        if nbr not in self.connectedNodes:
            self.connectedNodes[nbr] = cost

    def isVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        vertex = Vertex(key)
        self.numVertices+=1
        self.vertList[key] = vertex


    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t],cost)
        self.vertList[t].addNeighbour(self.vertList[f],cost)

def dijikstra(G,S):
    heap = [(0,S)]
    heapify(heap)
    G.vertList[S].distance = 0
    while len(heap) > 0:
        min_distance_vertex = heappop(heap)
        current_node = G.vertList[min_distance_vertex[1]]
        current_node.setVisited()
        for i in current_node.connectedNodes:
            if i.isVisited():
                continue
            if i.distance > current_node.distance + current_node.connectedNodes[i]:
                i.distance = current_node.distance + current_node.connectedNodes[i]

                
        while len(heap) > 0:
            heappop(heap)
        heap = [(G.vertList[i].distance,i) for i in G.vertList if not G.vertList[i].isVisited()]
        heapify(heap)



graph = Graph()
for i in range(9):
    graph.addVertex(i)
    graph.vertList[i].distance = float("Inf")

graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7)

dijikstra(graph,0)

for i in graph.vertList:
    print(graph.vertList[i].data,end=" ")
    print(graph.vertList[i].distance)


