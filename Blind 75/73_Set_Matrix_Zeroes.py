# Not Bad - we can still reduce space 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        setRowZero = [False] * ROWS
        setColZero = [False] * COLS
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    setRowZero[r] = True
                    setColZero[c] = True
                    
        for r in range(ROWS):
            for c in range(COLS):
                if setRowZero[r] or setColZero[c]:
                    matrix[r][c] = 0
                    
        # TC: O(m * n)
        # SC: O(m + n)
        
        
#Most Optimal O(1) space 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        setRowZero = False
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        setRowZero = True
                    
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if setRowZero:
            for c in range(COLS):
                matrix[0][c] = 0
                    
        # TC: O(m * n)
        # SC: O(1)