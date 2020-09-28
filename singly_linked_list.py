class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None

    def print_list(self) -> None:
        cur_node = self.head
        while cur_node:
            print(cur_node.data, '-> ', end="")
            cur_node = cur_node.next
        print('\n')

    def append(self, data: str) -> None:
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

    def prepend(self, data: str) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node: str, data: str) -> None:
        new_node = Node(data)
        cur_node = self.head

        # Find the node with data == prev_node_data
        while cur_node and cur_node.data != prev_node:
            cur_node = cur_node.next

        if cur_node is None:  # We can't find the node
            print("Previous node is not in the list")
            return

        # Otherwise we find the node with data == prev_node_data
        new_node.next = cur_node.next
        cur_node.next = new_node

    def delete_ndoe(self, data: str) -> None:
        """
        Two cases: 
        1. node to be deleted is head 
        2. node to be deleted is not head
        """
        cur_node = self.head

        # Case 1: delete head node
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return

        # Else Case 2: delete non-head node
        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:  # The node is not present in the list
            return

        # Delete cur_node
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        # If deleting head, i.e. pos == 0:
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        # Else:
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        # Delete cur_node
        prev.next = cur_node.next
        cur_node = None


llist = LinkedList()

llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.print_list()  # A -> B -> C -> D

llist.prepend('E')
llist.print_list()  # E -> A -> B -> C -> D

llist.insert_after_node("B", 'F')
llist.print_list()  # E -> A -> B -> F -> C -> D

llist.delete_ndoe('E')
llist.print_list()  # A -> B -> F -> C -> D

llist.delete_node_at_pos(0)
llist.print_list()  # B -> F -> C -> D

llist.delete_node_at_pos(1)
llist.print_list()  # B -> C -> D
