class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    def set_data(self, data):
        self.data = data

    def append_to_tail(self, last_data):
        last_node = Node(data=last_data)
        node = self
        while node.next != None:
            node = node.next
        node.next = last_node


test_node = Node(data=1)
test_node.append_to_tail(2)
test_node.append_to_tail(3)

node = test_node
while node != None:
    print("self: {0}, next: {1}, data: {2}".format(node, node.next, node.data))
    node = node.next
