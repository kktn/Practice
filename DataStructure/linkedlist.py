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

    def delete_node(self, head, data):
        # delete head
        if head.data == data:
            if head.next == None:
                return None
            head = head.next

        node = head
        while node.next != None:
            if node.next.data == data:
                node.next = node.next.next
            node = node.next
            if node == None:
                return head

        return head

def verify_linkedlist(head_node):
    node = head_node
    while node != None:
        # print("self: {0}, next: {1}, data: {2}".format(node, node.next, node.data))
        print("data: {0}".format(node.data))
        node = node.next

def main():
    head_node = Node(data=1)
    for data in range(2, 10):
        head_node.append_to_tail(data)
    head_node.append_to_tail(2)

    # Verify Delete
    print("Before delete")
    verify_linkedlist(head_node)
    # normal case
    print("Will delete 4")
    head_node = head_node.delete_node(head_node, 4)
    verify_linkedlist(head_node)
    # can't find the node
    print("Will delete 20 (List doesn't have 20.)")
    head_node = head_node.delete_node(head_node, 20)
    verify_linkedlist(head_node)
    # delete head node
    print("Will delete 1")
    head_node = head_node.delete_node(head_node, 1)
    verify_linkedlist(head_node)
    # delet 2 nodes
    print("Will delete 2")
    head_node = head_node.delete_node(head_node, 2)
    verify_linkedlist(head_node)

if __name__ == "__main__":
    main()
