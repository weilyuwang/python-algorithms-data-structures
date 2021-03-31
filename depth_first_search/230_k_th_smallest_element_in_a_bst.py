'''
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # recursively
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.result = None
        self.n = k
        
        def inorder(r):
            if not r:
                return
            inorder(r.left)
            self.n -= 1 
            if self.n == 0:
                self.result = r.val
                return
            inorder(r.right)
            
        inorder(root)
        return self.result
    

    # iteratively
    def kthSmallestIteratively(self, root: TreeNode, k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            root = root.right