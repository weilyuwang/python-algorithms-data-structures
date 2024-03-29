'''
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        
        # The height of a node is defined as the length of the longest downward path to a leaf node from that node.
        def height(root):
            if not root:
                return -1
            left = height(root.left)
            right = height(root.right)
            self.res = max(self.res, left + right + 2)
            
            return 1 + max(left, right)
        
        height(root)
        return self.res