from sys import stdin

class Node:
    def __init__(self,data,price):
        self.data = data
        self.rank = 0
        self.networkPrice = price
        self.parent = self



def find_root(node):
    if node != node.parent:
        node.parent = find_root(node.parent)
        return node.parent

    return node.parent

def calculate_price(parent_1,parent_2):
    
    if parent_2.networkPrice < parent_1.networkPrice:
        if parent_2.networkPrice >= 0:
            return parent_2.networkPrice
        else:
            return parent_1.networkPrice

    else:
        if parent_1.networkPrice >= 0:
            return parent_1.networkPrice
        else:
            return parent_2.networkPrice



def union(node_1,node_2):
    parent_1,parent_2 = find_root(node_1),find_root(node_2)
    min_price = calculate_price(parent_1,parent_2)
    if parent_1 == parent_2:
        return
    if parent_1.rank >parent_2.rank:
        parent_2.parent = parent_1
        parent_1.networkPrice = min_price
    else:
        parent_1.parent = parent_2
        parent_2.networkPrice = min_price
        if parent_1.rank == parent_2.rank:
            parent_2.rank+=1
    
    


N,M = map(int,stdin.readline().strip().split(" "))
queries=[]
for i in range(M):
    queries.append(tuple(map(int,stdin.readline().strip().split(" "))))
prices = []
for i in range(N):
    prices.append(int(stdin.readline()))
vertex = [Node(i,j) for i,j in zip(range(1,N+1),prices)]

for i in queries:
    union(vertex[i[0]-1],vertex[i[1]-1])
usage_dict = {}
for i in range(1,N+1):
    usage_dict[i] = False
sum=0
possible = True
min_cost = 10 ** 5
countDict = {}
for i in vertex:
    networkRoot = find_root(i)
    if networkRoot.data not in countDict:
        countDict[networkRoot.data] = True

    if networkRoot.networkPrice < 0:
        possible = False
        break

    
    if usage_dict[networkRoot.data] == False and networkRoot.networkPrice >= 0:
        if min_cost > networkRoot.networkPrice:
            min_cost = networkRoot.networkPrice
        sum+=networkRoot.networkPrice
        usage_dict[networkRoot.data] = True




count= 0 

for i in countDict:
    count+=1

        
if count == 1:
    print("0")
elif  not possible:
    print("-1")
else:
    print(sum+(count-2)*min_cost)
    

