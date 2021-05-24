'''
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''



from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")

        nums.sort()
        
        for i in range(0, len(nums) - 2):
            
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            lower = i + 1
            upper = len(nums) - 1
            
            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                
                if s == target:
                    return target
                    
                # update the closest number to target
                if abs(target - s) < abs(target - closest):
                    closest = s
                    
                if s < target:
                    lower += 1
                    
                    # skip duplicates
                    while lower < upper and nums[lower] == nums[lower - 1]:
                        lower += 1
                else:
                    upper -= 1
                    
                    # skip duplicates
                    while lower < upper and nums[upper] == nums[upper + 1]:
                        upper -= 1
                    
        return closest
