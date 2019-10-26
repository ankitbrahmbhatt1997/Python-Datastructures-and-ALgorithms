from sys import stdin,setrecursionlimit
setrecursionlimit(10000)

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

def calculatePossibilities(G):
    cc = connectedComponents(G)
    if len(cc) == 1:
        return 0
    a = cc[0]
    b = cc[1]
    answer = len(a)*len(b)
    sum=len(a)+len(b)
    for i in range(2,len(cc)):
        answer=answer+sum*len(cc[i])
        sum+=len(cc[i])
    return answer

fi = open("input.txt","r")
n,p = map(int,fi.readline().strip().split(" "))
G = Graph()
for i in range(0,n):
    G.addVertex(i)
for i in range(p):
    a1,a2 = map(int,fi.readline().strip().split(" "))
    G.addEdge(a1,a2)


print(calculatePossibilities(G))


