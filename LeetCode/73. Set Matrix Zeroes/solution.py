import copy


class Solution:
    #     def setZeroes(self, matrix: List[List[int]]) -> None:
    #         if not matrix:
    #             return None
    #         newMatrix = copy.deepcopy(matrix)

    #         for row in range(len(newMatrix)):
    #             for col in range(len(newMatrix[row])):
    #                 if newMatrix[row][col] == 0:
    #                     matrix = self.update(matrix, row, col)

    #     def update(self, matrix, row, col):
    #         for r in range(len(matrix)):
    #             matrix[r][col] = 0
    #             if r == row:
    #                 for c in range(len(matrix[r])):
    #                     matrix[r][c] = 0

    #         return matrix

    #     Time = O((n.m)^2) worse case - if entire matix is 0
    #      Space = O(n.m)

    # Better appraoch with reduced space
    #     def setZeroes(self, matrix: List[List[int]]) -> None:
    #         rows, cols = [False] * len(matrix), [False] * len(matrix[0])

    #         for r in range(len(matrix)):
    #             for c in range(len(matrix[r])):
    #                 if matrix[r][c] == 0:
    #                     rows[r] = True
    #                     cols[c] = True

    #         for r in range(len(matrix)):
    #             for c in range(len(matrix[r])):
    #                 if rows[r] or cols[c]:
    #                     matrix[r][c] = 0

    #   Time = O(n.m) or technically O(2(n.m))
    #   Space = O(n + m)

    # best solution with O(1) space - usinf first row and col as markers
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZeroTracker = False

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZeroTracker = True

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        if rowZeroTracker:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0


#   Time = O(n.m) or technically O(3(n.m))
#   Space = O(1)
