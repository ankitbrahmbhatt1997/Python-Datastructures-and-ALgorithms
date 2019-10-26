# from itertools import combinations
# from sys import stdin

# t = int(stdin.readline())
# for _ in range(t):
#     N, K1, K2, K3 = map(int, stdin.readline().strip().split(" "))
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     sum_array = []
#     for i in range(N):
#         sum_array.append(set(combinations(arr, i+1)))
#     print(sum_array)

from sys import stdin

class MaxHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0


    def percolate_up(self, i):
        while ((i-1)//2) >= 0:
            if self.heapList[i] > self.heapList[(i-1)//2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[(i-1)//2]
                self.heapList[(i-1)//2] = temp
            i = (i-1)//2

    def insert_element(self, element):
        self.heapList.append(element)
        self.currentSize += 1
        self.percolate_up(self.currentSize-1)
    
    def peek(self):
        return self.heapList[0]
   
    def max_child(self,i):
        if ((i*2)+2) > self.currentSize-1:
            return (i*2)+1
        else:
            if self.heapList[(i*2)+1] > self.heapList[(i*2)+2]:
                return (i*2)+1
            else:
                return (i*2)+2

    def percolate_down(self,i):
        while ((i*2)+1) < self.currentSize:
            maxChild = self.max_child(i)
            if self.heapList[i] < self.heapList[maxChild]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[maxChild] 
                self.heapList[maxChild]=temp
            i = maxChild



    
    def delete_max(self):
        self.heapList[0] = self.heapList[self.currentSize-1]
        self.heapList.pop()
        self.currentSize -= 1
        self.percolate_down(0)

    def build_heap(self,alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = alist
        while i > 0:
            self.percolate_down(i-1)
            i=i-1


t=int(stdin.readline())
while(t>0):
    t-=1
    n,k1,k2,k3=map(int,stdin.readline().split())
    arr=list(map(int,stdin.readline().split()))
    pq = MaxHeap()
    add=[]
    for i in range(len(arr)):
        su=arr[i]
        add.append(su)
        # pq.insert_element(su)
        
        for j in range(i+1,len(arr)):
            su+=arr[j]
            add.append(su)
            # pq.insert_element(su)

    pq.build_heap(add)
    
    # print(add[k1-1],add[k2-1],add[k3-1])
    k = 1
    limit = pq.currentSize
    answers=[]
    
    while k <= limit :
        top_element = pq.peek()
        
        pq.delete_max()
        if(k==k1):
            
            answers.append(top_element)
        if(k==k2):
            
            answers.append(top_element)
        if(k==k3):
            
            answers.append(top_element)
        k+=1
    
    print(answers[0],answers[1],answers[2])
            