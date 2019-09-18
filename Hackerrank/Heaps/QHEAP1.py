from sys import stdin

class BinaryHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0



    def insert_element(self,element):
        self.heapList.append(element)
        self.currentSize+=1
        self.siftUp(self.currentSize-1)

    def siftUp(self,i):
        while((i-1)//2)>=0:

            if self.heapList[i]<self.heapList[(i-1)//2]:
                self.heapList[i],self.heapList[(i-1)//2]=self.swap(self.heapList[i],self.heapList[(i-1)//2])

            i = (i-1)//2

    def siftDown(self,i):
        while ((i*2)+1) < self.currentSize:
            minChild = self.min_child(i)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i],self.heapList[minChild]=self.swap(self.heapList[i],self.heapList[minChild])
            i=minChild

    def delete_element(self,element):
        i = self.heapList.index(element)
        deletedElement = self.heapList[i]
        self.heapList[i] = self.heapList[self.currentSize-1]
        self.heapList.pop()
        self.currentSize-= 1
        self.siftDown(i)

    def peek(self):
        return self.heapList[0]



    def min_child(self,i):
        if ((i*2)+2) > self.currentSize-1:
            return (i*2)+1
        else:
            if self.heapList[(i*2)+1] < self.heapList[(i*2)+2]:
                return (i*2)+1
            else:
                return (i*2)+2

    def swap(self,element1,element2):
        element1,element2=element2,element1
        return element1,element2



t = int(stdin.readline())
heap = BinaryHeap()
for  _ in range(t):
    
    inp = list(map(int,stdin.readline().strip().split(" ")))
    operation = inp[0] 
    element =  inp[1] if len(inp) == 2  else 0

    if operation == 1:
        heap.insert_element(element)
    elif operation == 2:
        heap.delete_element(element)
    elif operation == 3:
        print(heap.peek())
        
        
        

