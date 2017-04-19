import linkedlist

class Queue:
    def __init__(self, data=None):
        if data == None:
            self.first = None
            self.last = None
        self.first = linkedlist.Node(data=data)
        self.last = self.first

    def enqueue(self, data):
        if self.first == None:
            self.first = linkedlist.Node(data=data)
            self.last = self.first

        self.last.next = linkedlist.Node(data=data)
        self.last = self.last.next

    def dequeue(self):
        if self.first == None:
            return None

        first = self.first
        self.first = self.first.next
        return first

print("Initialize queue with 1")
queue = Queue(1)

print("Add 2, 3, 4")
for i in range(2, 5):
    queue.enqueue(i)

print("dequeue twice")
for i in range(2):
    print(queue.dequeue().data)