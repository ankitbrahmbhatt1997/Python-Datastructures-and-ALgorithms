
# Thing to remember is not passing stack memory coz infinite recursion

import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self,data,score):
        self.data = data
        self.score = score
        self.parent = self
        self.rank = 1


def find_root(node):
    if node != node.parent:
        node.parent = find_root(node.parent)
        return node.parent
    return node.parent

def union_nodes(node_1,node_2):
    root_1,root_2 = find_root(node_1),find_root(node_2)
    if root_1 == root_2:
        return "-1"
    elif root_1.score > root_2.score:
        root_2.parent = root_1
    elif root_1.score < root_2.score:
        root_1.parent = root_2
    


t = int(sys.stdin.readline())

for _ in range(t):
    N = int(sys.stdin.readline())
    Scores = list(map(int,sys.stdin.readline().strip().split(" ")))
    vertex = [Node(i,s) for i,s in zip(range(1,N+1),Scores)]
    Q = int(sys.stdin.readline())
    for i in range(Q):
        query = list(map(int,sys.stdin.readline().strip().split(" ")))
        if query[0] == 0 :
            x,y = query[1],query[2]
            result = union_nodes(vertex[x-1],vertex[y-1])
            if result == "-1":
                print("Invalid query!")
        elif query[0] == 1:
            x = query[1]
            chef = find_root(vertex[x-1])
            print(chef.data)
  
    




    # if root_1.rank > root_2.rank:
    #     root_2.parent = root_1
    #     root_1.score = max(root_1.score,root_2.score)
    # else:
    #     root_1.parent = root_2
    #     root_2.score = max(root_1.score,root_2.score)
    #     if root_1.rank == root_2.rank:
    #         root_2.rank += 1