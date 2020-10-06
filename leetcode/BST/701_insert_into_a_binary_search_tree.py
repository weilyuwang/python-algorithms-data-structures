"""
701. Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, 
as long as the tree remains a BST after insertion. You can return any of them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        # Need to consider the case where root is None:
        if not root:
            return TreeNode(val)

        def insert(node, val):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)

        insert(root, val)
        return root
