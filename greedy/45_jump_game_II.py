'''
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 105

'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy approach: always jump to the place that will take us the farthest.
        jumps = 0
        current_jump_end = 0 # the end of the range that we can jump to
        farthest = 0 # the farthest place that we can reach
        for i in range(len(nums) - 1):
            # we continuously find the how far we can reach in the current jump
            farthest = max(farthest, i + nums[i])
            
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
        return jumps