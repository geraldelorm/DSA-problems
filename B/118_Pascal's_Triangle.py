class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            prevRow = triangle[-1]
            newRow = [1] * (len(prevRow) + 1)

            for j in range(1, len(newRow) - 1):
                newRow[j] = prevRow[j - 1] + prevRow[j]

            triangle.append(newRow)

        return triangle

        # TC: O(n^2)
        # SC: O(n) ~triangle returned 