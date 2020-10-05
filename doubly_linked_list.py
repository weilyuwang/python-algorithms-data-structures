class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        """
        Add new node of val data to the end of the list
        """
        if self.head is None:  # list is empty - make the node head
            new_node = Node(data)
            self.head = new_node
        else:   # Add to the end of the list
            new_node = Node(data)

            # Get the last node first
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        """
        Add new node of val data to the front of the list
        """
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)

            # Add the new node to the front of head
            self.head.prev = new_node
            new_node.next = self.head

            # Mark new head node
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur and cur.next:
            print(cur.data, '-> ', end="")
            cur = cur.next
        print(cur.data)


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.print_list()
