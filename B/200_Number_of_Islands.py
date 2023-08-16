class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(r, c):
            #dfs
            visited = set()
            to_visit = collections.deque()
            to_visit.append((r, c))

            while to_visit:
                r, c = to_visit.pop()
                grid[r][c] = "0"
                visited.add((r, c))

                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nei in neighbors:
                    if (nei not in visited and
                    (nei[0] > -1 and nei[0] < len(grid)) and
                    (nei[1] > -1 and nei[1] < len(grid[0])) and
                    grid[nei[0]][nei[1]] == "1"):
                        to_visit.append(nei)


        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_of_islands += 1
                    explore(r, c)


        return num_of_islands
        
        # TC: O(n * m)
        # SC: O(n * m) 