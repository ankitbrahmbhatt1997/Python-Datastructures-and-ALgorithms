from BinaryHeap import MinHeap
from sys import stdin



n = int(stdin.readline())
tasks = []
total_waiting_time=0
totalTime = 0
cookingPriority = MinHeap()
for _ in range(n):
    A,C = map(int,stdin.readline().strip().split(" "))
    tasks.append((A,C))

tasks.sort()

index=0

while tasks or cookingPriority.currentSize > 0:
    while tasks and tasks[index][0] <= totalTime:
        cookingPriority.insert_element(tasks.pop(0)[::-1])
    
    if cookingPriority.currentSize > 0:
        current_task = cookingPriority.peek()
        totalTime+=current_task[0]
        waitingTime = totalTime - current_task[1]
        total_waiting_time+=waitingTime
        cookingPriority.delete_min()
    else:
        cookingPriority.insert_element(tasks.pop(0)[::-1])
        current_task = cookingPriority.peek()
        totalTime = current_task[1]


    
        
    
print(total_waiting_time//n)




