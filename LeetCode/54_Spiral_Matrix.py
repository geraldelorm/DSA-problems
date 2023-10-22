class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        left, top  = 0, 0
        right, bottom = len(matrix[0]), len(matrix)
        
        
        while left < right and top < bottom:
            #get all items on top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            #get all items on right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            #check range is still valid
            if not(left < right and top < bottom):
                break
            
            #get all items on bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            #get all items on left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])          
            left += 1
            
            
        return res
    
    # TC: O(m * n)
    # SC: O(m * n)