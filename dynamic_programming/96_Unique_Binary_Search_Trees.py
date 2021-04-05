'''
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
Accepted
356,156
Submissions
651,724
'''

class Solution:
    def numTrees(self, n: int) -> int:
        """
        numTree[4] = numTree[0] * numTree[3] + (pick 1st node as root)
                      numTree[1] * numTree[2] + (pick 2nd node as root)
                      numTree[2] * numTree[1] + (pick 3rd node as root)
                      numTree[3] * numTree[0]   (pick 4th node as root)
        """
        # initialize DP array
        numTree = [0] * (n + 1)
        
        # 0 nodes = 1 tree, 1 nodes = 1 tree
        numTree[0], numTree[1] = 1, 1

        for numNodes in range(2, n + 1):
            for rootPos in range(1, numNodes + 1):
                left = rootPos - 1
                right = numNodes - rootPos
                numTree[numNodes] += numTree[left] * numTree[right]
        
        return numTree[n]
        