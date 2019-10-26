from sys import stdin,setrecursionlimit
setrecursionlimit(10000)
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

# def DFS_Recusrsive(G,S,connectedSet,distance):
    
#     G.vertList[S].setVisited()
#     G.vertList[S].distance = distance
#     connectedSet.append(G.vertList[S])
        
#     for i in G.vertList[S].connectedNodes:
#         if i.isVisited() == False:
#             connectedSet = DFS_Recusrsive(G,i.data,connectedSet,distance+1)
#     return connectedSet

def DFS(G,S):
    stack = []
    stack.append(S)
    connectedSet=[]
    distance=0
    G.vertList[S].distance = distance
    while len(stack) > 0 :
        currentVert = stack.pop()
        if G.vertList[currentVert].isVisited() == False:
            G.vertList[currentVert].setVisited()
            connectedSet.append(G.vertList[currentVert])

        for i in G.vertList[currentVert].connectedNodes:
            if i.isVisited() == False:
                i.distance = G.vertList[currentVert].distance + 1
                stack.append(i.data)
    return connectedSet

t=int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    G = Graph()
    for i in range(0,n):
        G.addVertex(i)
    for i in range(n-1):
        u,v=map(int,stdin.readline().strip().split(" "))
        G.addEdge(u,v)

    cc=DFS(G,1)
    max = cc[0]
    for i in cc:
        i.visited = False
        if i.distance > max.distance:
            max = i
    cc_2 = DFS(G,max.data)
    max = cc_2[0]
    for i in cc_2:
        if i.distance > max.distance:
            max = i
    if max.distance % 2 ==  0:
        print(max.distance//2)
    else:
        print((max.distance//2) + 1)
        

    

