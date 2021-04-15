'''
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
'''


class Solution:
    def maximalSquareTopDown(self, matrix: List[List[str]]) -> int:
        # DP recursive with Top-Down Memoization (cache)
        # Time complexity: O(m*n), space complexity: O(m*n)
        
        R, C = len(matrix), len(matrix[0])
        
        # Map each (r, c) -> Max Area (Max length of square)
        cache = {}
        
        def helper(r, c):
            if r >= R or c >= C:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            
            return cache[(r, c)]
        
        # compute and fill the cache recursively
        helper(0, 0)
        
        return max(cache.values()) ** 2

    def maximalSquareBottomUp(self, matrix: List[List[str]]) -> int:
            # DP with Bottom up
            R, C = len(matrix), len(matrix[0])
            dp = [[0] * (C + 1) for _ in range(R + 1)]
            
            maxLen = 0
            
            for i in range(1, R + 1):
                for j in range(1, C + 1):
                    if(matrix[i-1][j-1] == "1"):
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                        maxLen = max(maxLen, dp[i][j])
            
            return maxLen ** 2