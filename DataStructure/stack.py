import linkedlist

class Stack:
    def __init__(self, data=None):
        self.top = linkedlist.Node(data=data)

    def push(self, data):
        top = linkedlist.Node(data=data)
        top.next = self.top
        self.top = top

    def pop(self):
        if (self.top == None):
            return None
        top = self.top
        self.top = self.top.next
        return top

    def peek(self):
        return self.top

def verify_stack(stack):
    node = stack.top
    while node != None:
        print(node.data)
        node = node.next

print("Will initialize stack with 1")
stack = Stack(1)
verify_stack(stack)
print("Push 2, 3, 4 to stack")
stack.push(2)
stack.push(3)
stack.push(4)
verify_stack(stack)
print("Call Peek")
print(stack.peek().data)
print("Call Pop twice")
for i in range(2):
    print(stack.pop().data)
print("Call Peek")
print(stack.peek().data)

