class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def explore_to_edges(r, c):
            if (r, c) in visited: return 0
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 1

            grid[r][c] = "0"
            visited.add((r, c))

            return explore_to_edges(r + 1, c) + \
            explore_to_edges(r - 1, c) + \
            explore_to_edges(r, c + 1) + \
            explore_to_edges(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return explore_to_edges(r, c)

    # TC: O(n*m)
    # SC: O(n*m)


#Simplify this with just counting 