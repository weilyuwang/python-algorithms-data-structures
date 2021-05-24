'''
115. Distinct Subsequences
Hard


Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.


Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
there are 3 ways you can generate "rabbit" from S.

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
there are 5 ways you can generate "bag" from S.


'''


class Solution:
    def numDistinctTopDown(self, s: str, t: str) -> int:
        # Recursive / Top Down with memoization approach
        cache = {}
        
        def dfs(i, j):
            if j == len(t): # when we reach to the end of t, we get 1 solution
                return 1
            if i == len(s): # when we reach to the end of s, no solution
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            
            return cache[(i, j)]
        
        return dfs(0, 0)
  
    def numDistinctBottomUp(self, s: str, t: str) -> int:
        # dp[i][j] represents the number of solutions of aligning substring T[0..i] with S[0..j]
    
        T, S = len(t), len(s)
        
        dp = [[0] * (S + 1) for _ in range(T + 1)]
        
        # base case: fill the first row (when t == "") with 1s
        for j in range(len(dp[0])):
            dp[0][j] = 1
            
        for i in range(1, T + 1):
            for j in range(1, S + 1):
                if t[i - 1] == s[j - 1]:
                    # we could either include s[i] or not
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    # if T[i] != S[j], then the solution would be to ignore the character S[j] 
                    # and align substring T[0..i] with S[0..(j-1)]. Therefore, dp[i][j] = dp[i][j-1].
                    dp[i][j] = dp[i][j - 1]
                    
        return dp[-1][-1]

