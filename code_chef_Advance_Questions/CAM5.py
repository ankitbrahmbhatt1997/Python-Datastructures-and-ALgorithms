from sys import stdin,setrecursionlimit
setrecursionlimit(10000)


class Node:
    def __init__(self,data):
        self.data= data
        self.rank = 1
        self.parent = self
        

def find_parent(node):
    if node == node.parent:
        return node
    node.parent = find_parent(node.parent)
    return node.parent

def union(node_1,node_2):
    root_1,root_2=find_parent(node_1),find_parent(node_2)
    if root_1 == root_2:
        return 
    if root_1.rank > root_2.rank:
        root_2.parent = root_1
        
    else:
        root_1.parent = root_2
        if root_1.rank == root_2.rank:
            root_2.rank+=1

def find_groups(vertex):
    groups = set()
    for i in vertex:
        parent = find_parent(i)
        if parent not in groups:
            groups.add(parent)
    return groups

t= int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    e = int(stdin.readline())
    vertex = [Node(i) for i in range(n)]

    for i in range(e):
        a,b = map(int,stdin.readline().strip().split(" "))
        union(vertex[a],vertex[b])
    
    groups = find_groups(vertex)
    print(len(groups))
