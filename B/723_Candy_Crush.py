class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #Error check
        if not board: return board

        ROWS, COLS = len(board), len(board[0])
        stable = True

        #Mark Rows
        for r in range(ROWS):
            for c in range(COLS - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    stable = False
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])

        #Mark Cols
        for c in range(COLS):
            for r in range(ROWS - 2):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    stable = False
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])

        #Drop Candies ~ Gravity  
        for c in range(COLS):
            #move positive numbers down
            zero_start = ROWS - 1
            for r in range(ROWS - 1, -1, -1):
                if board[r][c] > 0:
                    board[zero_start][c] = board[r][c]
                    zero_start -= 1

            #fill zero spots with zero
            for r in range(zero_start, -1, -1):
                board[r][c] = 0

        #return or recurse
        return board if stable else self.candyCrush(board)


# TC: O(n^2 * m^2)
# SC: O(1)