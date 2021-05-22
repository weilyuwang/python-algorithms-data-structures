"""
698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
"""
from typing import List


class Solution:
    '''
    time complexity : O(k * 2^n)
    it takes the inner recursion 2^n time to find a good subset. 
    and we need to do this for k rounds
    '''
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if (sum(nums) % k != 0) or (k > len(nums)) or (max(nums) > sum(nums) // k):
            return False

        def backtrack(nums, k, visited, targetSubsetSum, curSubsetSum, nextIdx) -> bool:
            if k == 1:
                return True

            if curSubsetSum == targetSubsetSum:
                return backtrack(nums, k - 1, visited, targetSubsetSum, 0, 0)

            for i in range(nextIdx, len(nums)):
                if (not visited[i]) and (nums[i] + curSubsetSum <= targetSubsetSum):
                    visited[i] = True  # choose
                    if backtrack(nums, k, visited, targetSubsetSum, curSubsetSum + nums[i], i + 1):
                        return True
                    visited[i] = False  # unchoose/backtrack

            return False

        return backtrack(nums, k, [False] * len(nums), sum(nums) // k, 0, 0)


