'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]
      
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0            
            digitB = int(b[i]) if i < len(b) else 0
            
            total = digitA + digitB + carry
            carry = total // 2

            char = str(total % 2)
            res = char + res
        
        # Don't forget to check & add the carry (1) to the front
        if carry:
            res = str(carry) + res
            
        return res
