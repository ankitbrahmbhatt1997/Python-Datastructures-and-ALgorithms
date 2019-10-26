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


N = int(stdin.readline())
vertex = [Node(i) for i in range(1,2*N+1)]
for _ in range(N):
    G,B = map(int,stdin.readline().strip().split(" "))
    union_set(vertex[G-1],vertex[B-1])
    







max_value = min_value = vertex[0].size



for i in vertex:
    if max_value < i.size:
        max_value = i.size

    if min_value == 1:
        min_value = i.size
    

    elif min_value > i.size and i.size != 1:
        min_value = i.size

if min_value == 1:
    min_value=max_value


print(min_value,max_value)


# for i in vertex:
#     print(i.data,end=" ")
#     print(i.parent.data,end=" ")
#     print(i.rank,end=" ")
#     print(i.size)