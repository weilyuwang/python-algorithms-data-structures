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

    def len_iterative(self) -> int:
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def len_recursive(self, node: Node) -> int:
        if node is None:
            return 0

        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1: str, key_2: str) -> None:
        """
        Assume data entries are unique
        """
        if key_1 == key_2:
            return

       # Search for node 1 (curr_1) for key_1
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # Search for node 1 (curr_2) for key_2
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # Check if the two nodes both exist
        if not curr_1 or not curr_2:
            return

        # Swap:
        # First swap the two nodes
        # Need to check whether the node is head or not
        if prev_1:
            prev_1.next = curr_2  # move node 2 to node 1's previous position
        else:  # if prev_1 == None, then key_1 represents the head node
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1  # Move node 1 to node 2's previous position
        else:  # node2 is head
            self.head = curr_1  # move node1 to head

        # Then swap the nodes behind the two nodes
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

        # Above is the same as below:
        # temp = curr_1.next
        # curr_1.next = curr_2.next
        # curr_2.next = temp


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
llist.swap_nodes('B', 'C')
llist.print_list()  # E -> A -> C -> F -> B -> D ->
llist.swap_nodes('E', 'F')
llist.print_list()  # F -> A -> C -> E -> B -> D ->

llist.delete_ndoe('E')
llist.print_list()  # F -> A -> C -> B -> D ->

llist.delete_node_at_pos(2)
llist.print_list()  # F -> A -> B -> D ->

print(llist.len_iterative())
print(llist.len_recursive(llist.head))
