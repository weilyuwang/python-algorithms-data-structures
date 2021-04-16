'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] represents the minimum sum of the path 
        # from the index (i, j) to the bottom rightmost element.
        # dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        
        R, C = len(grid), len(grid[0])
        
        dp = [[0] * C for _ in range(R)]
        
        # Bottom up: from bottom right grid[R-1][C-1] to top left grid[0][0], final result will be grid[0][0]
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                if i == R-1 and j != C-1:
                    # when in bottom row, can only move to right
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif j == C-1 and i != R-1:
                    # when in right col, can only move to bottom
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif i != R-1 and j != C-1:
                    # normal case
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                else:
                    # when at bottom right (destination)
                    dp[i][j] = grid[i][j]
        
        return dp[0][0]