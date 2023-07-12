class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word): #search is completed
                return True
            #edge cases and false cases
            if ( r < 0 or c < 0 or
                r >= ROWS or
                c >= COLS or 
                (r, c) in path or
                board[r][c] != word[i]):
                return False
            
#             recursive dfs
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or
                  dfs(r, c - 1, i + 1))
    
            path.remove((r, c))
            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
                
        return False
    
#     Time = O(n * m * 4^n)
# Space = (n + m)