# 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)


    def transpose(self, matrix):
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    def reflect(self, matrix):
        n = len(matrix)
        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]

# O(m) where m is number of elements in matrix