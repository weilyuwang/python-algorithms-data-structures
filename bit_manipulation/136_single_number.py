'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''


from typing import DefaultDict, List


class Solution:
    def singleNumberV1(self, nums):
        counts = {}
        
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                del counts[n]
                
        return list(counts.keys())[0]


    def singleNumberV2(self, nums):
        hash_table = DefaultDict(int)

        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            

    def singleNumber(self, nums: List[int]) -> int:

        # XOR : O(1) space
        a = 0
        for n in nums:
            a ^= n
        return a
