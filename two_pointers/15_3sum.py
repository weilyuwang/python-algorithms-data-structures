'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        triplets = []

        nums.sort()
        
        for i in range(0, len(nums) - 2):
            
            if nums[i] > 0:
                break
            
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            lower = i + 1
            upper = len(nums) - 1
            
            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                if s == 0:
                    triplets.append((nums[i], nums[lower], nums[upper]))
                    lower += 1
                    upper -= 1
                    
                    # skip duplicates
                    while lower < upper and nums[lower] == nums[lower - 1]: 
                        lower += 1
                    while lower < upper and nums[upper] == nums[upper + 1]:
                        upper -= 1
                    
                elif s < 0:
                    lower += 1
                else:
                    upper -= 1
                    
        return triplets
