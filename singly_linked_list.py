class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
