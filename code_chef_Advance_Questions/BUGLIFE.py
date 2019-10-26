from sys import stdin,setrecursionlimit
setrecursionlimit(1000000)


class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.connectedNodes = {}
        self.color=None

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


def DFS_Recusrsive(G,S,color):
    
    G.vertList[S].setVisited()
    G.vertList[S].color = color
    for i in G.vertList[S].connectedNodes:
        oppositeColor = not color
        if color == i.color:
            return False
        if i.isVisited() == False:
            if(not DFS_Recusrsive(G,i.data,oppositeColor)):
                return False
    return True



def connected_components_bipartite(G):
    for i in G.vertList:
        if G.vertList[i].isVisited() == False:
            if not DFS_Recusrsive(G,i,True):
                return False
    return True


t = int(stdin.readline())
for _ in range(t):
    bugs,interactions = map(int,stdin.readline().strip().split(" "))
    G = Graph()
    for i in range(1,bugs+1):
        G.addVertex(i)
    for i in range(interactions):
        i,j =  map(int,stdin.readline().strip().split(" "))
        G.addEdge(i,j)
    answer = connected_components_bipartite(G)
    
    print("Scenario #{}:".format(_+1))
    if answer == True:
        print("No suspicious bugs found!")
    else:
        print("Suspicious bugs found!")

