# DFS recursive
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def mark_island(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return

            grid[r][c] = "V"

            mark_island(r - 1, c)  # top
            mark_island(r + 1, c)  # down
            mark_island(r, c - 1)  # left
            mark_island(r, c + 1)  # right

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1
                    mark_island(r, c)  # recursive DFS

        return islands
    # Time = O(N) - N is size of the matix
    # Space = O(1) - if resursive calll stack is ignored


# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands, visited = 0, set()

        def mark_island_bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for rd, cd in directions:
                    r = row + rd
                    c = col + cd

                    if (r in range(rows) and
                        c in range(cols) and
                        (r, c) not in visited and
                            grid[r][c] == "1"):

                        visited.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    mark_island_bfs(r, c)  # recursive DFS

        return islands

    # Time = O(N) - N is size of the matix
    # Space = O(1)


# DFS - iterative
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands, visited = 0, set()

        def mark_island_bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.pop()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for rd, cd in directions:
                    r = row + rd
                    c = col + cd

                    if (r in range(rows) and
                        c in range(cols) and
                        (r, c) not in visited and
                            grid[r][c] == "1"):

                        visited.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    mark_island_bfs(r, c)  # recursive DFS

        return islands

    # Time = O(N) - N is size of the matix
    # Space = O(1)
