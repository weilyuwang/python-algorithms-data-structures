'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''


class Solution:
    # DP with complexity of O(n) + O(n) space 
    def trap1(self, height: List[int]) -> int:
        result = 0
        maxHeightLeft, maxHeightRight, minMaxHeight = [0] * len(height), [0] * len(height), [0] * len(height)
        for i in range(1, len(height)):
            maxHeightLeft[i] = max(maxHeightLeft[i-1], height[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            maxHeightRight[i] = max(maxHeightRight[i+1], height[i+1])
            
        for i in range(len(height)):
            minMaxHeight[i] = min(maxHeightLeft[i], maxHeightRight[i])
            water = minMaxHeight[i] - height[i] if minMaxHeight[i] - height[i] > 0 else 0
            result += water
            
        return result
        

    
    # Two-pointers with complexity of O(n) + O(1) space 
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res