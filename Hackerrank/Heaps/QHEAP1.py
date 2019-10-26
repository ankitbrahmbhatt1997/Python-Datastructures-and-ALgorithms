from sys import stdin

from BinaryHeap import MinHeap


t = int(stdin.readline())
heap = MinHeap()
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
        
        
        

