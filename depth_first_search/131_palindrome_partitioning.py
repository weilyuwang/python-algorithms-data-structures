'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curlist = []
        
        def dfs(i):
            if i >= len(s):
                res.append(curlist.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrom(s, i, j):
                    # add current substring in the currentList
                    curlist.append(s[i:j+1])
                    dfs(j+1)
                    # backtrack and remove the current substring from currentList
                    curlist.pop()
        dfs(0)
        return res
        
    def isPalindrom(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True