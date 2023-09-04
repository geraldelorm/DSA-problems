class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row, col, direction):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 

            grid[row][col] = 0
            path_signature.append(direction)

            dfs(row + 1, col, "T")
            dfs(row - 1, col, "D")
            dfs(row, col + 1, "R")
            dfs(row, col - 1, "L")
            path_signature.append("-END")

        distinc_islands = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    path_signature = []
                    dfs(r, c, "START-")
                    if path_signature:
                        distinc_islands.add("".join(path_signature))

        return len(distinc_islands)

# TC: O(m.n)
# SC: O(m.n)