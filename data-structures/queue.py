from collections import deque


class ListQueue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # O(1) Add to right (tail)
    def enqueue(self, item):
        self.items.append(item)

    # O(n) Remove from left (head) - require shifting all the rest elements in the array
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    # Peek leftmost (head)
    def peek(self):
        if not self.is_empty():
            return self.items[0].value

    def size(self):
        return len(self.items())

    def __len__(self):
        return self.size()

    def __repr__(self):
        return '-'.join([str(item.value)for item in self.items])


class DequeQueue(object):
    '''
    Queue in Python can be implemented using deque class from the collections module.
    Deque is preferred over list in the cases where we need quicker
    append and pop operations from both the ends of container,
    as deque provides an O(1) time complexity for append and pop operations
    as compared to list which provides O(n) time complexity.
    '''

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    # O(1) Add to right (tail)
    def enqueue(self, item):
        self.items.append(item)

    # O(1) Remove from left (head)
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

    # Peek leftmost (head)
    def peek(self):
        if not self.is_empty():
            return self.items[0].value

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __repr__(self):
        return '-'.join([str(item.value) for item in self.items])

