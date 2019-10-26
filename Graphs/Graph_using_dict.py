class Vertex:
    def __init__(self,key):
        self.data = key
        self.connectedNodes = {}

    def addNeighbour(self,nbr,cost=0):
        if nbr not in self.connectedNodes:
            self.connectedNodes[nbr] = cost

    def getConnections(self):
        return self.connectedNodes.keys()







class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    def addVertex(self,key):
        self.numVertices+=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        
        self.vertList[f].addNeighbour(self.vertList[t],cost)


g = Graph()


for i in range(6):
    g.addVertex(i)

g.addEdge(2,3,0)

for i in g.vertList:
    print(g.vertList[i].data)
    print(g.vertList[i].getConnections())