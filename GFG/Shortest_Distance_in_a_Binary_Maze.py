#User function Template for python3

from typing import List
from heapq import heapify, heappop, heappush
'''
{{1, 1, 1, 1},
 {1, 1, 0, 1},
 {1, 1, 1, 1},
 {1, 1, 0, 0},
 {1, 0, 0, 1}}

'''
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        p_queue = []
        ROWS, COLS = len(grid), len(grid[0])
        heappush(p_queue, [0, source])
        
        grid[source[0]][source[1]] = 0
        
        while p_queue:
            distance, pos  = heappop(p_queue)
            
            if pos == destination:
                return distance
                
            row, col = pos
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 0
                    heappush(p_queue, [distance + 1, [new_row, new_col]])
                    
                    
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
        print("~")
# } Driver Code Ends