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
        result = []
        # First sort the array
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                # If the lowest val of a, b, c is greater than 0, break
                break

            # Skip duplicates
            if i == 0 or nums[i - 1] != nums[i]:
                # Run two sum on nums[i+1:]
                self.twoSum(nums, i, result)

        return result

    def twoSum(self, nums: List[int], i: int, result: List[List[int]]) -> None:
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum == 0:
                result.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                # Skip duplicates
                while lo < hi and nums[lo - 1] == nums[lo]:
                    lo += 1
            elif sum > 0:
                hi -= 1
            else:
                lo += 1
