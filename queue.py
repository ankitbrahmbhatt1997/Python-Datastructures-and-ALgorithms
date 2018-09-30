class Queue:

    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def enqueue(self, elem):
        self.list.insert(0, elem)

    def dequeue(self):
        self.list.pop()


q1 = Queue()


print(q1.isEmpty())
q1.enqueue(2)
print(q1.isEmpty())
