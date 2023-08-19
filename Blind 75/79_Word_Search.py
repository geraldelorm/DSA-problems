class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def search(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or 
             r >= ROWS or c >= COLS or 
             board[r][c] != word[i] or (r, c) in visited):
                return False

            visited.add((r, c))

            res = (search(r + 1, c, i + 1) or 
            search(r - 1, c, i + 1) or 
            search(r, c + 1, i + 1) or 
            search(r, c - 1, i + 1))

            visited.remove((r, c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if search(r, c, 0):
                        return True

        return False

        # TC: O(n^3^L) n = boardsize & L = len(word) as we have 3 branches as were search the
        # SC: O(L) 