'''
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
from typing import List


class Solution:
    
    # O(n)
    def bruteForce(self, array):
        products = [1 for _ in range(len(array))]

        for i in range(len(array)):
            product = 1
        for j in range(len(array)):
            if i != j:
                product *= array[j]
        products[i] = product
    
        return products

    # O(n)
    def threeLoops(self, array):
        products = [1 for _ in range(len(array))]
        leftProducts = [1 for _ in range(len(array))]
        rightProducts = [1 for _ in range(len(array))]
        
        lp = 1
        for i in range(len(array)):
            leftProducts[i] = lp
            lp *= array[i]
            
        rp = 1
        for i in reversed(range(len(array))):
            rightProducts[i] = rp
            rp *= array[i]
            
        for i in range(len(array)):
            products[i] = leftProducts[i] * rightProducts[i]
            
        return products


    # O(n) space-optimized
    def twoLoops(self, array):
        products = [1 for _ in range(len(array))]

        lp = 1
        for i in range(len(array)):
            products[i] = lp
            lp *= array[i]
            
        rp = 1
        for i in reversed(range(len(array))):
            products[i] *= rp
            rp *= array[i]
            
        return products


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.twoLoops(nums)


if __name__ == "__main__":
    solution = Solution()
    sample_input = [1,2,3,4]
    sample_output = [24,12,8,6]
    
    assert solution.productExceptSelf(sample_input) == sample_output
    print("Test passed")