class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self) -> None:
        cur = self.head
        while cur and cur.next:
            print(cur.data, '-> ', end="")
            cur = cur.next
        print(cur.data)

    def append(self, data) -> None:
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

    def prepend(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data) -> None:
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

    def delete_ndoe(self, data) -> None:
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

    def swap_nodes(self, key_1, key_2) -> None:
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

        # Return if the node can't be found
        if not curr_1:
            return

        # Search for node 2 (curr_2) for key_2
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # Return if the node can't be found
        if not curr_2:
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

    def reverse_iterative(self):
        """
        A -> B -> C -> D -> None
        None <- A <- B <- C <- D 
        """
        # Keep track of prev and curr node
        prev = None
        cur = self.head
        while cur:
            # Flipping arrows while moving along
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next
        # Remember to reset the head
        self.head = prev  # cur is None when the while loop breaks

    def reverse_recursive(self):
        """
        Recursively reverse the linked list
        """
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next
            _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def remove_duplicates(self):
        """
        Original list:
        1 -> 6 -> 1 -> 4 -> 2 -> 2 -> 4 -> None

        Remove duplicates:
        1 -> 6 -> 4 -> 2 -> None
        """
        cur = self.head
        prev = None

        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                # Remove/Skip the current/duplicated node:
                prev.next = cur.next
            else:
                # If have not encountered the element before
                dup_values[cur.data] = 1
                prev = cur

            cur = cur.next

    def print_nth_from_last(self, n):
        '''
        Method 1:
        Calculate the length of linked list first then count down
        '''
        # total_len = self.len_iterative()
        # cur = self.head
        # while cur:
        #     if total_len == n:
        #         print(f"{n}th to the last node is: {cur.data}\n")
        #         return cur

        #     total_len -= 1
        #     cur = cur.next

        # if not cur:
        #     return None

        '''
        Method 2:
        Two pointers: fast & slow pointer
        fast pointer is n nodes ahead of slow pointer
        if fast pointer reaches to the end of the list,
        then it means that the slow pointer must point to the nth-to-last node
        '''
        fast = self.head
        slow = self.head

        # Move fast pointer n steps ahead of slow pointer
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1

        if not fast:
            print(f"{n} is greater than the length of the linked list!")
            return

        while fast:
            slow = slow.next
            fast = fast.next

        print(f"The {n}th-to-last node is {slow.data}")
        return slow.data

    def rotate(self, k):
        """
        rotate the list to right, with respect to the kth node (the pivot)
        i.e. shift all the nodes after kth node to the front of the list
        e.g.
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                       p         q
        k = 4
        result:
        5 -> 6 -> 1 -> 2 -> 3 -> 4 -> None
        """
        p = self.head  # p: kth node
        q = self.head  # q: last node

        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        # Now p points to the kth node

        while q:
            prev = q
            q = q.next

        q = prev
        # Now q points to the last node

        # the last node (q) is now linked to the original head
        q.next = self.head
        self.head = p.next  # the new head is the (k+1)th node - p.next
        p.next = None  # p is the new end


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

llist.reverse_iterative()
llist.print_list()

llist.append('D')
llist.append('G')
llist.append('A')
llist.append('F')
llist.print_list()
llist.remove_duplicates()
llist.print_list()

llist.print_nth_from_last(3)

llist.print_list()
llist.rotate(3)
llist.print_list()
