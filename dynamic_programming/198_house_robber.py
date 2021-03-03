'''
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

'''



class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     rob1, rob2 = 0, 0
        
    #     # [rob1, rob2, n, n+1, ...]
        
    #     for n in nums:
    #         temp = max(n + rob1, rob2)
    #         rob1 = rob2
    #         rob2 = temp
            
    #     return rob2
    
    def rob(self, nums: List[int]) -> int:
        
        # if nums length <= 2: return the result directly
        if len(nums) <= 2:
            return 0 if len(nums) == 0 else max(nums)
        
        # dp(k) = Largest amount that you can rob from the first k houses.
        # dp[k] = max(dp[k-2] + house[k], dp[k-1])
        dp = list(range(len(nums)))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[-1]