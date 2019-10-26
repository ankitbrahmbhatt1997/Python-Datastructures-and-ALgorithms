class Vertex:
    def __init__(self,data):
        self.data = data
        self.distance = float("Inf")
        self.connectedNodes = {}

    def addNeighbour(self,nbr,cost=0):
        if nbr not in self.connectedNodes:
            self.connectedNodes[nbr] = cost

    def isVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.vertList = []
        self.numVertices = 0

    def addVertex(self,key):
        vertex = Vertex(key)
        self.numVertices+=1
        self.vertList.append(vertex)


    def addEdge(self,f,t,cost=0):
        self.vertList[f].addNeighbour(self.vertList[t],cost)

def bellmanFord(G,S):

    source = G.vertList[S]
    source.distance = 0
    for _ in range(G.numVertices-1):
        for i in G.vertList:
            for j in i.connectedNodes:
                if j.distance > i.distance+i.connectedNodes[j]:
                    j.distance = i.distance+i.connectedNodes[j]
        













g = Graph()
for i in range(5):
    g.addVertex(i) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3)

bellmanFord(g,0)

for i in g.vertList:
    print(i.data,end=" ")
    print(i.distance)