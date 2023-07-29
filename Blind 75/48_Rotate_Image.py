class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        
        while left < right:
            top, buttom = left, right
            for i in range(right - left):
                #store top_left value temporarily
                top_left = matrix[top][left + i]
                
                #move buttom_left to top_left
                matrix[top][left + i] = matrix[buttom - i][left]
                
                #move buttom_right to buttom_left
                matrix[buttom - i][left] = matrix[buttom][right - i]
                
                #move top_right to buttom_right
                matrix[buttom][right - i] = matrix[top + i][right]
                
                #move saved top_left to top_left
                matrix[top + i][right] = top_left
                

            left += 1
            right -= 1
            
        return matrix
    

    # TC: O(N^2)
    #SC: O(1)