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
    def numDistinct(self, s: str, t: str) -> int:
        # Recursive / Top Down with memoization approach
        cache = {}
        
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            
            return cache[(i, j)]
        
        return dfs(0, 0)

