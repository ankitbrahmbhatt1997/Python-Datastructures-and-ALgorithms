from sys import stdin
class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.distance = 0

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

def DFS_Recusrsive(G,S,connectedSet,distance):
    
    G.vertList[S].setVisited()
    G.vertList[S].distance = distance
    connectedSet.append(G.vertList[S])
        
    for i in G.vertList[S].connectedNodes:
        if i.isVisited() == False:
            connectedSet = DFS_Recusrsive(G,i.data,connectedSet,distance+1)
    return connectedSet

n = int(stdin.readline())
G = Graph()
for i in range(1,n+1):
    G.addVertex(i)
for i in range(n-1):
    u,v=map(int,stdin.readline().strip().split(" "))
    G.addEdge(u,v)

cc=DFS_Recusrsive(G,1,[],0)
max = cc[0]
for i in cc:
    print(i.data,end=" ")
    print(i.distance)
    i.visited = False
    if i.distance > max.distance:
        max = i
cc_2 = DFS_Recusrsive(G,max.data,[],0)
max = cc_2[0]
for i in cc_2:
    if i.distance > max.distance:
        max = i
# print(max.distance)
