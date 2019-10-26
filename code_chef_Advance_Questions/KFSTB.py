from sys import stdin,setrecursionlimit
setrecursionlimit(10000)



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
    return Stack

def calculateNumberOfPaths(sorted_vertex,G,destination):
    dp = [0]*G.numVertices
    dp[destination-1] = 1
    for i in range(len(sorted_vertex)-1,-1,-1):
        for j in G.vertList[i+1].connectedNodes:
            dp[i]+=dp[j.data-1]%(10**9+7)

    return dp


t = int(stdin.readline())
for _ in range(t):
    C,B,S,T = map(int,stdin.readline().strip().split(" "))
    G = Graph()
    for i in range(1,C+1):
        G.addVertex(i)

    for i in range(B):
        X,Y = map(int,stdin.readline().strip().split(" "))
        G.addEdge(X,Y)

    top_sort_vertex = topologicalSort(G)
    dp = calculateNumberOfPaths(top_sort_vertex,G,T)

    print(dp[S-1]%(10**9+7))

    
    
