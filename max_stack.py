"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. 
            If you find more than one maximum elements, only remove the top-most one.
"""


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or self.max_stack[-1] <= x:
            self.max_stack.append(x)

    def pop(self) -> int:
        if self.max_stack[-1] == self.stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    # O(n) time complexity + O(n) space complexity
    def popMax(self) -> int:
        cur_max = self.peekMax()

        # We can pop until we find that maximum,
        # then push the popped elements back on the stack.
        temp = []
        while self.stack[-1] != cur_max:
            temp.append(self.pop())
        # val is the first maximum on self.stack
        val = self.stack.pop()
        self.max_stack.pop()

        for item in temp[::-1]:
            self.push(item)

        return val


maxStack = MaxStack()
maxStack.push(5)
maxStack.push(1)
print(maxStack.stack, maxStack.max_stack)
print(maxStack.popMax())
print(maxStack.stack, maxStack.max_stack)
print(maxStack.peekMax())
