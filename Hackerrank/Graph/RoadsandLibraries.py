from sys import stdin

class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}

    def addNeighbour(self,nbr,cost=0):
        if nbr not in self.connectedNodes:
            self.connectedNodes[nbr] = True

    def isVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True  

class Graph:
    def __init__(self):
        self.numVertices = 0
        self.vertList = {}


    def addVertex(self,key,cost=0):
        newVertex = Vertex(key)
        self.numVertices+=1
        self.vertList[key] = newVertex

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t],cost)
        self.vertList[t].addNeighbour(self.vertList[f],cost)


def DFS_Recusrsive(G,S,connectedSet):
    if G.vertList[S].isVisited() == False:
        G.vertList[S].setVisited()
        connectedSet.append(S)
        
    for i in G.vertList[S].connectedNodes:
        if i.isVisited() == False:
            connectedSet = DFS_Recusrsive(G,i.data,connectedSet)
    return connectedSet



def connectedComponents(G):
    cc=[]
    for i in G.vertList:
        if G.vertList[i].isVisited() == False:
            cc.append(DFS_Recusrsive(G,i,[]))
    return cc

def calculateMinimumCost(G,c_lib,c_road):
    cost = 0
    cc = connectedComponents(G)
    for i in cc:
        cost+=c_lib+(c_road*(len(i)-1))
    return cost

fi = open("input.txt","r")
t = int(fi.readline())
for _ in range(t):
    n,m,c_lib,c_road = map(int,fi.readline().strip().split(" "))
    G = Graph()
    for i in range(1,n+1):
        G.addVertex(i)
    for i in range(m):
        u,v = map(int,fi.readline().strip().split(" "))
        G.addEdge(u,v)
    if c_lib <= c_road:
        print(n*c_lib)
    else:
        print(calculateMinimumCost(G,c_lib,c_road))



