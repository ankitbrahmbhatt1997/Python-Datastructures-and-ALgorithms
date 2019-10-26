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
        self.vertList[t].addNeighbour(self.vertList[f],cost)



def BFS(G,S):
    queue = []
    queue.append(S)
    G.vertList[S].setVisited()
    while len(queue) > 0 :
        currentVert = queue.pop(0)
        for i in G.vertList[currentVert].connectedNodes:
            if i.isVisited() == False:
                i.setVisited()
                queue.append(i.data)
                print(i.data,end=" ")


def DFS(G,S):
    stack = []
    stack.append(S)
    while len(stack) > 0 :
        currentVert = stack.pop()
        if G.vertList[currentVert].isVisited() == False:
            G.vertList[currentVert].setVisited()
            print(currentVert,end=" ")

        for i in G.vertList[currentVert].connectedNodes:
            if i.isVisited() == False:
                
                stack.append(i.data)



def DFS_Recusrsive(G,S):
    if G.vertList[S].isVisited() == False:
        G.vertList[S].setVisited()
        print(S,end=" ")
        
    for i in G.vertList[S].connectedNodes:
        if i.isVisited() == False:
            DFS_Recusrsive(G,i.data)
    return


# def connectedComponents(G):
#     cc=[]
#     for i in G.vertList:
#         if G.vertList[i].isVisited() == False:
#             cc.append(DFS_Recusrsive(G,i,""))

#     for i in cc:
#         print(i)

                  



g = Graph()


for i in range(5):
    g.addVertex(i)

# g.addEdge(1, 2) 
# g.addEdge(1, 4) 
# g.addEdge(1, 7) 
# g.addEdge(2, 5) 
# g.addEdge(2, 6) 
# g.addEdge(5, 7) 
# g.addEdge(4, 6)
# g.addEdge(3, 6)
g.addEdge(1, 0);  
g.addEdge(0, 2);  
g.addEdge(2, 1);  
g.addEdge(0, 3);  
g.addEdge(1, 4);  


DFS(g,0)



