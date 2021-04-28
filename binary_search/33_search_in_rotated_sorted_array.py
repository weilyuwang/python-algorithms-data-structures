'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

Follow up: Can you achieve this in O(log n) time complexity?
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # if mid is in the left sorted portion 
            # - compare with the first element in the left portion
            if nums[l] <= nums[mid]:
                # 1) if target is > mid element and target is in the left portion
                if target > nums[mid]:
                    l = mid + 1
                # 2) if target is < mid element and is in the right portion
                elif target < nums[l]:
                    l = mid + 1
                # 3) target is < mid and is in the left portion
                else:
                    r = mid - 1
               
            # if mid is in the right sorted portion 
            else:
                # 1) if target < mid
                if target < nums[mid]:
                    r = mid - 1
                # 2) if target > mid and target is in the left portion
                elif target > nums[r]:
                    r = mid - 1
                # 3) if target > mid and target is in the right portion
                else:
                    l = mid + 1
        
        return -1 