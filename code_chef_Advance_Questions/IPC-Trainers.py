
from sys import stdin
from collections import defaultdict

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







def calculate_minimum_sadness(N, D,info_dict):
    # info.sort()
    pq=MaxHeap()
    for i in range(D):
        
        # while info and info[0][0] <= i+1:
        #     pq.insert_element(info.pop(0)[::-1])

        if i+1 in info_dict:
            
            if len(info_dict[i+1]) == 1:
                
                pq.insert_element((info_dict[i+1][0][1],info_dict[i+1][0][0],i+1))  
            elif len(info_dict[i+1]) > 1:
                
                for j in info_dict[i+1]:
                    
                    pq.insert_element((j[1],j[0],i+1)) 

            
        if pq.currentSize > 0:
            pq.heapList=teach_a_lecture(pq)
    
   
    minimumSadness=0
    for j in pq.heapList:
        minimumSadness+= j[0]*j[1]
    return minimumSadness




def teach_a_lecture(pq):
    heapList = pq.heapList
    if heapList[0][1] > 1:
        reducedDay = list(heapList[0])
        reducedDay[1] = reducedDay[1]-1
        pq.heapList[0] = tuple(reducedDay)
    else:
        pq.delete_max()
    
    return pq.heapList





t = int(stdin.readline())
for i in range(t):
    N, D = map(int, stdin.readline().strip("").split(" "))
    
    info_dict=defaultdict(list)
    for j in range(N):
        d, t, s = map(int, stdin.readline().strip().split(" "))
        
        if d in info_dict:
           
            ne = info_dict[d]
            ne.append((t,s))
            
            info_dict[d] = ne
        else:
            
            info_dict[d] = [(t,s)]

        
    print(calculate_minimum_sadness(N, D,info_dict))
