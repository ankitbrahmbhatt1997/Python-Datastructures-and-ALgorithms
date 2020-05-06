from heapq import heappush,heappop,heapify
from sys import stdin

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
    heap = [(0,0,S)]
    heapify(heap)
    G.vertList[S].distance = 0
    mdt = 0
    while len(heap) > 0:
        min_distance_vertex = heappop(heap)
        current_node = G.vertList[min_distance_vertex[2]]
        if current_node.isVisited() == True:
            continue
        mdt+=min_distance_vertex[1]
        current_node.setVisited()
        for i in current_node.connectedNodes:
            if i.distance >= current_node.distance + current_node.connectedNodes[i]:
                i.distance = current_node.distance + current_node.connectedNodes[i]
                heappush(heap,(i.distance,current_node.connectedNodes[i],i.data))
    return mdt

def prims(G,S):
    heap = [(0,S)]
    heapify(heap)
    G.vertList[S].distance = 0
    minimum_distance = 0
    while len(heap) > 0:
        min_distance_vertex = heappop(heap)
        current_node = G.vertList[min_distance_vertex[1]]
        if current_node.isVisited() == True:
                continue
        minimum_distance+=current_node.distance
        
        current_node.setVisited()
        for i in current_node.connectedNodes:
            if i.distance >  current_node.connectedNodes[i]:
                i.distance =  current_node.connectedNodes[i]
                heappush(heap,(i.distance,i.data))
    return minimum_distance
            



t = int(stdin.readline())
for _ in range(t):
    n,m = map(int,stdin.readline().strip().split(" "))
    g = Graph()
    for i in range(n):
        g.addVertex(i)
        g.vertList[i].distance = float("Inf")
    for i in range(m):
        u,v,cost = map(int,stdin.readline().strip().split(" "))
        g.addEdge(u,v,cost)
    

    Australian_distance = dijikstra(g,0)
    Answer = True
    for i in range(n):
        current_node = g.vertList[i]
        if not current_node.isVisited():
            Answer = False
            break

        
        current_node.distance = float("Inf")
        current_node.visited = False
    
    if not Answer:
        print("NO")
        continue
    newZealand_distance = prims(g,0)
    if Australian_distance == newZealand_distance:
        print("YES")
    else:
        print("NO")







