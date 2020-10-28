class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur and cur.next:
            print(cur.data, '-> ', end="")
            cur = cur.next
        print(cur.data)

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

    def delete(self, key):
        cur = self.head
        while cur:
            # if found the key
            if cur.data == key:
                # if the node to delete is the head
                if cur == self.head:
                    # Case 1: if the head is the only node
                    if not cur.next:
                        self.head = None

                        # Clear cur node
                        cur = None

                        return
                    # Case 2: if the head has 1 or more nodes behind
                    else:
                        nxt = cur.next

                        self.head = nxt
                        nxt.prev = None

                        # Clear cur node and the nodes it was pointing to
                        cur.next = None
                        cur = None

                        return
                 # If the node to delete is not head node
                else:
                    # Case 3: the node is not the last node, i.e. cur.next is not None
                    if cur.next:
                        nxt = cur.next
                        prev = cur.prev
                        prev.next = nxt
                        nxt.prev = prev

                        # Clear cur node and the nodes it was pointing to
                        cur.next = None
                        cur.prev = None
                        cur = None

                        return
                    # Case 4: if the node is the last node, i.e. cur.next is None
                    else:
                        prev = cur.prev
                        prev.next = None

                        # Clear cur node and the nodes it was pointing to
                        cur.prev = None
                        cur = None

                        return
            # Keep searching for the key
            cur = cur.next

    def delete_node(self, node: Node):
        cur = self.head
        while cur:
            # if found the node
            if cur == node:
                # if the node to delete is the head
                if cur == self.head:
                    # Case 1: if the head is the only node
                    if not cur.next:
                        self.head = None

                        # Clear cur node
                        cur = None

                        return
                    # Case 2: if the head has 1 or more nodes behind
                    else:
                        nxt = cur.next

                        self.head = nxt
                        nxt.prev = None

                        # Clear cur node and the nodes it was pointing to
                        cur.next = None
                        cur = None

                        return
                 # If the node to delete is not head node
                else:
                    # Case 3: the node is not the last node, i.e. cur.next is not None
                    if cur.next:
                        nxt = cur.next
                        prev = cur.prev
                        prev.next = nxt
                        nxt.prev = prev

                        # Clear cur node and the nodes it was pointing to
                        cur.next = None
                        cur.prev = None
                        cur = None

                        return
                    # Case 4: if the node is the last node, i.e. cur.next is None
                    else:
                        prev = cur.prev
                        prev.next = None

                        # Clear cur node and the nodes it was pointing to
                        cur.prev = None
                        cur = None

                        return
            # Keep searching for the key
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            # Move to next - note that now the next node is cur.prev not cur.next
            cur = cur.prev
        if tmp:
            # set new head
            self.head = tmp.prev

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append((p.data, q.data))
                q = q.next
            p = p.next
        return pairs


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
dllist.delete(5)
dllist.print_list()  # 1 -> 6 -> 2 -> 3 -> 10 -> 4 -> 7
dllist.delete(6)
dllist.print_list()  # 1 -> 2 -> 3 -> 10 -> 4 -> 7
dllist.delete(7)
dllist.print_list()  # 1 -> 2 -> 3 -> 10 -> 4
dllist.delete(10)
dllist.print_list()  # 1 -> 2 -> 3 -> 4
dllist.reverse()
dllist.print_list()  # 4 -> 3 -> 2 -> 1
dllist.append(1)
dllist.append(2)
dllist.append(5)
dllist.append(4)
dllist.print_list()  # 4 -> 3 -> 2 -> 1 -> 1 -> 2 -> 5 -> 4
dllist.remove_duplicates()
dllist.print_list()  # 4 -> 3 -> 2 -> 1 -> 5
print(dllist.pairs_with_sum(5))
