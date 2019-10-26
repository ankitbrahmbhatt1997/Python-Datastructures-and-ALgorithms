from sys import stdin

class Node:
    def __init__(self,data):
        self.data = data
        self.rank=0
        self.parent=self
        self.size = 1



def union_set(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
        x.size+=y.size
        y.size = 1
    else:
        x.parent = y
        y.size+=x.size
        x.size=1
        if x.rank == y.rank:
            y.rank += 1


def find_set(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
        
    return x.parent

N,Q = map(int,stdin.readline().strip().split(" "))
people = [Node(i) for i in range(1,N+1)]

for _ in range(Q):
    query = list(stdin.readline().strip().split(" "))
    if query[0] == "M":
        I,J = int(query[1]),int(query[2])
        union_set(people[I-1],people[J-1])
    elif query[0] == "Q":
        I = int(query[1])
        parent = find_set(people[I-1])
        print(parent.size)
        