from itertools import product

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get all border nodes 
        ROWS, COLS = len(board), len(board[0])

        row_borders = list(product(range(ROWS), [0, COLS - 1]))
        col_borders = list(product([0, ROWS - 1], range(COLS)))

        borders = row_borders + col_borders
        # mark all bordernodes and 0 nodes connected to them as non flipable 
        def mark(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return 
            board[r][c] = "N"
            mark(r + 1, c)
            mark(r - 1, c)
            mark(r, c + 1)
            mark(r, c - 1)

        for border in borders:
            r, c = border
            if board[r][c] == "O":
                #mark and find adjusent "O" nodes ~ dfs
                mark(r, c)

        # flip all other O nodes to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"    
                if board[r][c] == "N":
                    board[r][c] = "O"       


        # TC: O(N)
        # SC: O(N)
