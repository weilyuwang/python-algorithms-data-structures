"""
Stack Data Structure
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()  # will raise error if items is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # last item

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items


# s = Stack()
# s.push('A')
# s.push('B')
# print(s.get_stack())
# s.push('C')
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
# s.push('E')
# print(s.get_stack())
# s.pop()
# print(s.is_empty())
# print(s.peek())
# s.pop()
# print(s.is_empty())
