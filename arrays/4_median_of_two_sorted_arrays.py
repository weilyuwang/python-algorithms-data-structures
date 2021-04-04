'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:                                                                                     
             
Input: nums1 = [2], nums2 = []
Output: 2.00000       

Constraints:
                                                              
nums1.length == m                                                                                                                                                                      
nums2.length == n
0 <= m <= 1000                                      
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
 

Follow up: The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        # Let A be the smaller array
        if len(B) < len(A):
            A, B = B, A
            
        total = len(nums1) + len(nums2)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  #A
            j = half - i - 2  #B
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # check if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd 
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aright > Bright:
                # left part of A is too large, need to decrease the left part of A
                r = i - 1
            else:
                # left part of A is too small, need to increase the left part of A
                l = i + 1
                
