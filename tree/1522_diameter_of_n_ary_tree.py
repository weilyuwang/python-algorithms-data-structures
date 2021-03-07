'''
1522. Diameter of N-Ary Tree

Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [1, 104].

'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.diameter = 0
        
        def height(node):
            """ return the height of the node """            
            if node is None:
                return -1
            
            # select the top two heights:
            max_height_1, max_height_2 = -1, -1
            for child in node.children:
                h = height(child) + 1
                if h > max_height_1:
                    max_height_1, max_height_2 = h, max_height_1
                elif h > max_height_2:
                    max_height_2 = h
            
            self.diameter = max(self.diameter, max_height_1 + max_height_2 + 2)
            
            return max_height_1
        
        height(root)
        return self.diameter