class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        L = len(matrix)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for r in range(L):
            for c in range(L):
                if 1 <= matrix[r][c] <= L:
                    if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                        return False
                    rows[r].add(matrix[r][c])
                    cols[c].add(matrix[r][c])
                else:
                    return False

        return True

        # Time = O(n^2)
        # Space = O(n^2)
