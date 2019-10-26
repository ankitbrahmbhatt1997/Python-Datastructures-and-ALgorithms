class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
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



def topologicalSortUtil(G,S,Stack):
    
    G.vertList[S].setVisited()
        
        
    for i in G.vertList[S].connectedNodes:
        if i.isVisited() == False:
            topologicalSortUtil(G,i.data,Stack)

    Stack.insert(0,S)
    return


def topologicalSort(G):
    Stack=[]
    for i in G.vertList:
        if G.vertList[i].isVisited() == False:
            topologicalSortUtil(G,i,Stack)
    print(*Stack)


G =Graph()
for i in range(4):
    G.addVertex(i)
G.addEdge(0, 1)
G.addEdge(0, 2) 
G.addEdge(0, 3) 
G.addEdge(2, 0) 
G.addEdge(1, 3)
topologicalSort(G)

