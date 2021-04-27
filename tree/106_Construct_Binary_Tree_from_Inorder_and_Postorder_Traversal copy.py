'''
106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values. ******* IMPORTANT *******
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    # O(N^2) Bad Runtime and has side effect to postorder input list
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val) 

        root.right = self.buildTree(inorder[mid+1:], postorder) 
        root.left = self.buildTree(inorder[:mid], postorder)

        return root
    
    # O(N) runtime and no modifications on the postorder list
    def buildTreev2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # postorder: [{root.left} + {root.right} + root]
        # inorder: [ {root.left} + root + {root.right} ]
        
        value_to_idx = dict()
        for idx, value in enumerate(inorder):
            value_to_idx[value] = idx
            
        def build(inorder, postorder, in_start, in_end, post_start, post_end):
            if in_start <= in_end:
                root = TreeNode(postorder[post_end])
                in_idx = value_to_idx[root.val]
                in_idx_delta = in_idx - in_start
                root.left = build(inorder, postorder,
                                  in_start, in_idx - 1,
                                  post_start, post_start + in_idx_delta - 1)
                root.right = build(inorder, postorder,
                                   in_start + in_idx_delta + 1, in_end,
                                   post_start + in_idx_delta, post_end - 1)
                return root
            else:
                return None

        return build(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)