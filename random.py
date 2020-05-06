from sys import stdin

class Node:
    def __init__(self,data):
        self.data = data
        self.rank=0
        self.parent=self
        self.size = 1
        self.total_edges = 0



def union_set(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        x.total_edges+=1
        return
    if x.rank > y.rank:
        y.parent = x
        x.size+=y.size
        x.total_edges+=1
        y.size = 0
    else:
        x.parent = y
        y.size+=x.size
        y.total_edges+=1
        x.size=0
        if x.rank == y.rank:
            y.rank += 1


def find_set(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
        
    return x.parent


n,m = map(int,stdin.readline().strip().split(" "))
vertex = [Node(i) for i in range(1,n+1)]
for i in range(m):
    u,v = map(int,stdin.readline().strip().split(" "))
    union_set(vertex[u-1],vertex[v-1])
total_roads_needed = 0
for i in vertex:
    if i.size > 0:
        n1 = i.size - 1
        roads_needed = n1**2 - (n1*(n1-1))//2
        
        roads_needed = roads_needed - i.total_edges
        total_roads_needed+=roads_needed

print(total_roads_needed)


