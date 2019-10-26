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

    

class MinHeap:
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
        self.heapList[i] = self.heapList[self.currentSize-1]
        self.heapList.pop()
        self.currentSize-= 1
        self.siftDown(i)
    
    def delete_min(self):
        self.heapList[0] = self.heapList[self.currentSize-1]
        self.heapList.pop()
        self.currentSize -= 1
        self.siftDown(0)

    

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





n = int(stdin.readline())

median=0
minHeap = MinHeap()
maxHeap = MaxHeap()
for _ in range(n):
    value = int(stdin.readline())
    if value > median:
        minHeap.insert_element(value)
    else:
        maxHeap.insert_element(value)
    
    if maxHeap.currentSize > minHeap.currentSize and maxHeap.currentSize - minHeap.currentSize >1:
        minHeap.insert_element(maxHeap.peek())
        maxHeap.delete_max()
    elif minHeap.currentSize > maxHeap.currentSize and minHeap.currentSize - maxHeap.currentSize >1:
        maxHeap.insert_element(minHeap.peek())
        minHeap.delete_min()
    if maxHeap.currentSize == minHeap.currentSize:
        median= (maxHeap.peek() + minHeap.peek())/2
    elif maxHeap.currentSize > minHeap.currentSize:
        median = maxHeap.peek()
    else:
        median = minHeap.peek()
    
    print("%.1f"%median)



