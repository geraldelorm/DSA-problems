#Brute Force
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(rows):
            seen = set()
            for n in rows:
                if n == ".":
                    continue
                if int(n) > 9 or int(n) < 0 or n in seen:
                    return False
                seen.add(n)
            return True
    
        def valid_sub(grid):
            seen = set()
            ROWS, COLS = len(grid),len(grid[0])
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c]  == ".":
                        continue
                    if int(grid[r][c]) > 9 or int(grid[r][c]) < 0 or grid[r][c] in seen:
                        return False
                    seen.add(grid[r][c])
            return True
            
        ROWS, COLS = len(board),len(board[0])
        #validate all rows
        for r in range(ROWS):
            if not valid(board[r]):
                return False
        
        #validate all columns
        for c in range(COLS):
            cols = [r[c] for r in board]
            if not valid(cols):
                return False
            
        #validate all 3 * 3 sub-grids
        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                sub_grid = [
                    [board[r][c], board[r][c+ 1], board[r][c + 2]],
                    [board[r+ 1][c], board[r + 1][c+ 1], board[r + 1][c + 2]],
                    [board[r+ 2][c], board[r + 2][c+ 1], board[r + 2][c + 2]]
                           ]
                if not valid_sub(sub_grid):
                    return False
                            
        return True
    
    # TC: O(n^2)
    # SC: O(n^2)


#Not really optimized but cleaner
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = collections.defaultdict(set)
        cols_set = collections.defaultdict(set)
        squares_set = collections.defaultdict(set) 
        #we can get unique suqre index by doing integer division
            
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_set[r] or 
                    board[r][c] in cols_set[c] or 
                    board[r][c] in squares_set[(r//3, c//3)]):
                    return False
                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                squares_set[(r//3, c//3)].add(board[r][c])
                            
        return True
    
    # TC: O(n^2)
    # SC: O(n^2)