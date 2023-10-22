class NumMatrix:

    def __init__(self, matrix: List[List[int]]): #TC: O(n*m)
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_ = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            leftPrefix = 0
            for c in range(COLS):
                leftPrefix += matrix[r][c]
                above = self.sum_[r][c + 1]
                self.sum_[r + 1][c + 1] = above + leftPrefix 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: #TC: O(1)
        sum_col2 = self.sum_[row2 + 1][col2 + 1] - self.sum_[row1][col2 + 1]
        sum_col1 = self.sum_[row2 + 1][col1] - self.sum_[row1][col1]
        return sum_col2 - sum_col1


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)