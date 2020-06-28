class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self,n):
        self.data.append(n)

    def dequeue(self):
        self.data = self.data[1:]

    def front(self):
        print(self.data[0])
        return self.data[0]




q1 = Queue()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.front()
q1.dequeue()
q1.front()

print(q1.data)