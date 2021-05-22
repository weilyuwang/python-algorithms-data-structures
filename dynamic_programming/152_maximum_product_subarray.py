'''
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            cur = nums[i]
            temp_max_so_far = max(cur, max_so_far * cur, min_so_far * cur)
            min_so_far = min(cur, max_so_far * cur, min_so_far * cur)
            max_so_far = temp_max_so_far
            
            result = max(max_so_far, result)
        
        return result
