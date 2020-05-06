from sys import stdin
from heapq import heappush,heappop,heapify

class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.distance = None

    def addNeighbour(self,nbr,cost=0):
        if nbr not in self.connectedNodes:
            visited=False
            self.connectedNodes[nbr] = (cost,visited)

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

    def setEdgeAsVisited(self,f,t):
        edgeData = self.vertList[f].connectedNodes[self.vertList[t]]
        edgeDataList = list(edgeData)
        edgeDataList[1] = True
        self.vertList[f].connectedNodes[self.vertList[t]] = tuple(edgeDataList)
        self.vertList[t].connectedNodes[self.vertList[f]] = tuple(edgeDataList)


    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t],cost)
        self.vertList[t].addNeighbour(self.vertList[f],cost)


def dijikstra(G,S):
    heap = [(0,0,1,S)]
    heapify(heap)
    G.vertList[S].distance = 0
    while len(heap) > 0:
        min_distance_vertex = heappop(heap)
        current_node = G.vertList[min_distance_vertex[3]]
        
        for i in current_node.connectedNodes:
            edgeData = current_node.connectedNodes[i]
            if edgeData[1] == True:
                continue
            
            if current_node.data == S :
                if i.distance > current_node.distance + edgeData[0]:
                    i.distance = current_node.distance + edgeData[0]
                    heappush(heap,(i.distance,edgeData[0],1,i.data))
                    G.setEdgeAsVisited(current_node.data,i.data)
            else:
                difference = 0
                if min_distance_vertex[1] - edgeData[0] > 0:
                    difference = 1
                if min_distance_vertex[1] - edgeData[0] < 0:
                    difference = -1
                correctPath = False
                if difference == min_distance_vertex[2]:
                    correctPath = True
                if i.distance > current_node.distance + edgeData[0] and correctPath:
                    i.distance = current_node.distance + edgeData[0]
                    heappush(heap,(i.distance,edgeData[0],-1*difference,i.data))
                    G.setEdgeAsVisited(current_node.data,i.data)




                
            


t = int(stdin.readline())
for _ in range(t):
    n,m = map(int,stdin.readline().strip().split(" "))
    G = Graph()
    for i in range(1,n+1):
        G.addVertex(i)
        G.vertList[i].distance = float("Inf")
    for i in range(m):
        u,v,cost = map(int,stdin.readline().strip().split(" "))
        G.addEdge(u,v,cost)
    Source,Sink = map(int,stdin.readline().strip().split(" "))
    dijikstra(G,Source)
    for i in G.vertList:
        print(G.vertList[i].data,end=" ")
        print(G.vertList[i].distance)