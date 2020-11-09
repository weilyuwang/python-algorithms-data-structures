from collections import deque


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            # [:-1]: pop the '-' char in the end
            print("\npreorder:")
            return self.preorder_print(tree.root, '')[:-1]

        elif traversal_type == "inorder":
            print("\ninorder:")
            return self.inorder_print(tree.root, '')[:-1]
        elif traversal_type == "postorder":
            print("\npostorder:")
            return self.postorder_print(tree.root, '')[:-1]
        elif traversal_type == "levelorder":
            print("\nlevelorder:")
            return self.levelorder_print(tree.root)[:-1]
        else:
            print(f"\nTraversal type {traversal_type} is not supported.")
            return None

    def preorder_print(self, start, traversal):
        """ Root -> Left -> Right """
        if start:
            traversal += f"{start.value}-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):
        """ Left -> Root -> Right """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += f"{start.value}-"
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        """ Left -> Right -> Root """
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += f"{start.value}-"

        return traversal

    def levelorder_print(self, start):
        """
        Need to leverage Queue data structure to traverse level by level
        """
        if start is None:
            return

        queue = DequeQueue()
        queue.enqueue(start)

        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'

            # dequeue the current node and then enqueue its children
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def height(self):
        '''
        Recursively calculate the height of each node
        '''
        def height_helper(node: Node):
            if node is None:
                return -1

            left_height = height_helper(node.left)
            right_height = height_helper(node.right)

            return 1 + max(left_height, right_height)

        return height_helper(self.root)

    def size_recursive(self):
        def size_helper(node: Node):
            if node is None:
                return 0
            left_size = size_helper(node.left)
            right_size = size_helper(node.right)

            return 1 + left_size + right_size

        return size_helper(self.root)

    def size_iterative(self):
        if self.root is None:
            return 0

        stack = deque()
        stack.append(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)

        return size


'''
       1
     /   \
    2      3
   / \    /  \
  4   5  6    7

'''

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))

print('\nHeight of the tree:')
print(tree.height())
print(tree.size_iterative())
print(tree.size_recursive())
