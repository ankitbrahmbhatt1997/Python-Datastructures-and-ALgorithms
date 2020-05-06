from sys import stdin
from heapq import heappush,heappop,heapify

class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.distance = None
        self.direction = 0

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







def dijikstra(G,S,heights,cost):
    heap = [(0,0,S)]
    heapify(heap)
    G.vertList[S].distance = 0
    while len(heap) > 0:
        min_distance_vertex = heappop(heap)
        current_node = G.vertList[min_distance_vertex[2]]
        current_node.setVisited()
        for i in current_node.connectedNodes:
            if i.isVisited():
                continue
            direction = 0
            if heights[current_node.data-1] > heights[i.data-1]:
                direction = -1
            elif heights[current_node.data-1] < heights[i.data-1]:
                direction = 1
            else:
                direction = min_distance_vertex[1]
            cost = 0
            if direction != min_distance_vertex[1]:
                cost = costs[current_node.data - 1]

            if i.distance > current_node.distance + cost:
                i.distance = current_node.distance + cost
                i.direction = direction

                
        while len(heap) > 0:
            heappop(heap)
        heap = [(G.vertList[i].distance,G.vertList[i].direction,i) for i in G.vertList if not G.vertList[i].isVisited()]
        heapify(heap)


N,R = map(int,stdin.readline().strip().split(" "))
heights = list(map(int,stdin.readline().strip().split(" ")))
costs = list(map(int,stdin.readline().strip().split(" ")))
G = Graph()
for i in range(1,N+1):
    G.addVertex(i)
    G.vertList[i].distance = float("Inf")
for i in range(R):
    u,v = map(int,stdin.readline().strip().split(" "))
    G.addEdge(u,v)
dijikstra(G,1,heights,costs)

    
print(G.vertList[N].distance)




