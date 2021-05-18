'''
41. First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.


Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
'''


class Solution:
    def firstMissingPositive(self, nums):
        """
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
        3. after removing all the numbers greater than or equal to n, all the numbers remaining are smaller than n. 
            If any number i appears, we add n to nums[i] which makes nums[i]>=n. 
            Therefore, if nums[i]<n, it means i never appears in the array and we should return i.
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): 
            # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)): 
            # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n


    def firstMissingPositiveV2(self, nums):
        """
        instead of += n to index i, we can * -1 to indicates that number i appears in the list
        """
        for i in range(len(nums)):
            # remove all negative elements
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1  # nums[i] < 0 means number i+1 appears in the list
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1) # any number > len(nums) works
            # ignore those numbers that are larger than len(nums)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0: # nums[i] >= 0 means number i+1 is missing
                return i

        # default case
        return len(nums) + 1
