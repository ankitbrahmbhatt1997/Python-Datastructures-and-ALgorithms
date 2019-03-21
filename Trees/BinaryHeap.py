# Binary Heap using a list
# Normally pointers are required but because binary heap is a complete Binary Tree, children and parents can be calculated using arithmetic operations


class BinaryHeap:
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
        max=self.heapList[0]
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

    


heap = BinaryHeap()
# heap.build_heap([11,20,44,66,20,6])
heap.insert_element(11)
heap.insert_element(20)
heap.insert_element(44)
heap.insert_element(66)
heap.insert_element(20)
heap.insert_element(6)
# heap.insert_element(21)
# heap.delete_max()
# heap.delete_max()

print("Size of the heap  " + str(heap.currentSize))
print("All elements in the heap are   " +
      ",".join(list(map(str, heap.heapList))))

print(heap.heapList)

# [66, 20, 44, 20, 11, 6]