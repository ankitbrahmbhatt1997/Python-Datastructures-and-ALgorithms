# from sys import stdin,setrecursionlimit
# setrecursionlimit(10000)

# class Node:
#     def __init__(self,data):
#         self.data= data
#         self.rank = 1
#         self.parent = self
#         self.setLength = 1

# def find_parent(node):
#     if node == node.parent:
#         return node
#     node.parent = find_parent(node.parent)
#     return node.parent

# def union(node_1,node_2):
#     root_1,root_2=find_parent(node_1),find_parent(node_2)
#     if root_1 == root_2:
#         return 
#     if root_1.rank > root_2.rank:
#         root_2.parent = root_1
#         root_1.setLength+=1
#     else:
#         root_1.parent = root_2
#         root_2.setLength+=1
#         if root_1.rank == root_2.rank:
#             root_2.rank+=1

# def find_groups(vertex):
#     groups = set()
#     for i in vertex:
#         parent = find_parent(i)
#         if parent not in groups:
#             groups.add(parent)
#     return groups


from sys import stdin,setrecursionlimit
setrecursionlimit(1000)

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


def evaluate(G):
    groups = connectedComponents(G)
    ways = 1
    for i in groups:
        ways=(ways % (10**9 + 7) *len(i) % (10**9 + 7)) %(10**9 + 7)
    return (len(groups),ways)




t = int(stdin.readline())

for _ in range(t):
    n,m = map(int,stdin.readline().strip().split(" "))
    G = Graph()
    for i in range(1,n+1):
        G.addVertex(i)

    for i in range(m):
        i,j =  map(int,stdin.readline().strip().split(" "))
        G.addEdge(i,j)
    u,v = evaluate(G)
    print(str(u)+" "+str(v))
