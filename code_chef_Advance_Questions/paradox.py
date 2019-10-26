from sys import stdin
from sys import stdin
class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.existence = True

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

def DFS_Recusrsive(G,S):
    
    G.vertList[S].setVisited()
    for i in G.vertList[S].connectedNodes:
        if i.isVisited() == False:
            if G.vertList[S].existence == i.existence:
                return False
            if not DFS_Recusrsive(G,i.data):
                return False
    return True

N = int(stdin.readline())
while N > 0:
    G = Graph()
    for i in range(N):
        G.addVertex(i+1)
    for i in range(N):
        values = list(stdin.readline().strip().split(" "))
        value = int(values[0])
        existence = False if values[1] == "false" else True
        if i+1 != value:
            G.addEdge(i+1,value)
            G.vertList[i+1].existence = not existence
        G.vertList[value].existence = existence
        
    
    isParadox = DFS_Recusrsive(G,1)
    if isParadox:
        print("PARADOX")
    else:
        print("NOT PARADOX")

    N = int(stdin.readline())
