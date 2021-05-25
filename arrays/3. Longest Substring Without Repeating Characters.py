'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = {}
        cur_sub_start = 0
        cur_len = 0
        longest = 0
        
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= cur_sub_start:
                # We found a duplicate, start over with a new substring
                # the new start index would be right after the index of the duplicate letter
                cur_sub_start = sub[letter] + 1
            
            sub[letter] = i 
            
            # Update current and longest len
            cur_len = i - cur_sub_start + 1
            longest = max(cur_len, longest)
        
        return longest
