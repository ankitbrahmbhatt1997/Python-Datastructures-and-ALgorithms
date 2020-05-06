from heapq import heappush,heappop,heapify
from sys import stdin

class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.distance = None

    def addNeighbour(self,nbr,cost=0):
        
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
        if current_node.isVisited() == True:
            continue
        current_node.setVisited()
        for i in current_node.connectedNodes:
            if i.distance > current_node.distance + current_node.connectedNodes[i]:
                i.distance = current_node.distance + current_node.connectedNodes[i]
                heappush(heap,(i.distance,i.data))


# file = open("input.txt","r")

t = int(stdin.readline())
for _ in range(t):
    n,m = map(int,stdin.readline().strip().split(" "))
    G = Graph()
    for i in range(1,n+1):
        G.addVertex(i)
        G.vertList[i].distance = float("Inf")
    for i in range(m):
        u,v,cost = map(int,stdin.readline().strip().split(" "))
        vertex_u = G.vertList[u]
        vertex_v = G.vertList[v]
        if vertex_v in vertex_u.connectedNodes and vertex_u.connectedNodes[vertex_v] < cost:
            continue
        G.addEdge(u,v,cost)
    s = int(stdin.readline())
    dijikstra(G,s)
    for i in range(1,n+1):
        if i == s:
            continue
        if G.vertList[i].distance == float("Inf"):
            print("-1",end=" ")
        else:
            if i == n :
                print(G.vertList[i].distance)
            else:
                print(G.vertList[i].distance,end=" ")

            