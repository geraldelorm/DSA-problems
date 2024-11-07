#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        island_set = set()
        visited = set()
        
        def get_valid_neighbors(row, col):
            neighbors = []
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                if (0 <= new_row < ROWS and 0 <= new_col < COLS and 
                grid[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                    neighbors.append((new_row, new_col))
                    visited.add((new_row, new_col))

            return neighbors

        def explore_island(base, row, col, unique_key):
            unique_key.append(row - base[0])
            unique_key.append(col - base[1])

            for new_row, new_col in get_valid_neighbors(row, col):
                explore_island(base, new_row, new_col, unique_key)

        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    unique_key = []
                    explore_island([row, col], row, col, unique_key)
                    island_set.add(tuple(unique_key))
                   
        return len(island_set)
