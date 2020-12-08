'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def coords(t, b, l, r):
            '''
            Return the coords in spiral order given the 4 values

            t t t t
            l     r
            l     r
            l b b r 
            '''
            # 1. return numbers in top row, from left to right
            for col in range(l , r+1):  # [l, r]
                yield t, col
            # 2. return numbers in right col, from top to bottom
            for row in range(t+1, b+1):  # [t+1, l]
                yield row, r
                
            # Then, we need to check if r > l and b > t
            if r > l and b > t:
                # 3. return numbers in bottom row, from right to left
                for col in range(r-1, l, -1):   # [r-1, l+1]
                    yield b, col
                # 4. return numbers in left col, from bottom to top    
                for row in range(b, t, -1):  # [b, t+1]
                    yield row, l
                
                
        if not matrix: return []
        
        # m x n matrix:
        m, n = len(matrix), len(matrix[0])    

        # Define 4 vars to start with:
        # t: index_top_row
        # b: index_bottom_row
        # l: index_left_col
        # r: index_right_col

        t, b, l, r = 0, m - 1, 0, n - 1
        
        ans = []
        
        while t <= b and l <= r:
            for row, col in coords(t, b, l, r):
                ans.append(matrix[row][col])
            
            # Move to the inner cycle
            t += 1
            b -= 1
            l += 1
            r -= 1
            
        return ans