class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r,c) in visited or 
                heights[r][c] < prevHeight):
                return 
            
            visited.add((r,c))
            
            dfs(r - 1,c, visited, heights[r][c])
            dfs(r + 1,c, visited, heights[r][c])
            dfs(r,c + 1, visited, heights[r][c])
            dfs(r,c - 1, visited, heights[r][c])
            
        for c in range(COLS): #traverse pacific top to down & atlantic down to top
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS): #traverse pacific top to down & atlantic down to top
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
        
    # Time = O(n * m)
    # Space = O(n * m)