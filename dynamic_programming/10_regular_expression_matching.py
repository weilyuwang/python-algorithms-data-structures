'''
10. Regular Expression Matching
Hard

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial). 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
 

Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

'''


class Solution(object):
    # Top-Down with Memoization
    def isMatch(self, s, p):
        cache = {}
        
        # dp(i, j): does s[i:] and p[j:] match
        def dfs(i,j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False
    
        return dfs(0, 0)


    # Bottom-up
    def isMatch(self, s, p):
        # initialize dp: (len(s) + 1) x (len(p) + 1)
        # dp[i][j]: does s[i:] and p[j:] match
        # final answer would be dp[0][0]
        
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                else:
                    dp[i][j] = match and dp[i+1][j+1]

        return dp[0][0]