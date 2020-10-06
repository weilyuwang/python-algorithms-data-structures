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
            self.head = new_node

    def add_after_node(self, key, data):
        """
        Add data after key
        """
        cur = self.head
        while cur:
            # If found the node with value == key
            if cur.data == key:
                if cur.next is None:  # If it is the last node
                    self.append(data)
                    return
                else:
                    new_node = Node(data)
                    nxt = cur.next  # Need to store the next node
                    cur.next = new_node
                    new_node.next = nxt
                    nxt.prev = new_node
                    new_node.prev = cur
            # Keep searching for key
            cur = cur.next

    def add_before_node(self, key, data):
        """
        Add data before key
        """
        cur = self.head
        while cur:
            # If found key
            if cur.data == key:
                if cur.prev is None:  # if key is the head node
                    self.prepend(data)  # Simply prepend the data
                    return
                else:
                    new_node = Node(data)
                    prev = cur.prev  # Need to store the previous node
                    new_node.next = cur
                    prev.next = new_node
                    cur.prev = new_node
                    new_node.prev = prev
            # Keep searching for key
            cur = cur.next

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
dllist.print_list()  # 5 -> 1 -> 2 -> 3 -> 4
dllist.add_after_node(3, 10)
dllist.print_list()  # 5 -> 1 -> 2 -> 3 -> 10 -> 4
dllist.add_after_node(4, 7)
dllist.print_list()  # 5 -> 1 -> 2 -> 3 -> 10 -> 4 -> 7
dllist.add_before_node(2, 6)
dllist.print_list()  # 5 -> 1 -> 6 -> 2 -> 3 -> 10 -> 4 -> 7
