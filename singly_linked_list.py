class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, '-> ', end="")
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        # First check if the current list is empty
        if self.head is None:
            self.head = new_node
            return

        # If no empty, traverse to the very end of the list and append the new item
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.prepend('E')
llist.print_list()
