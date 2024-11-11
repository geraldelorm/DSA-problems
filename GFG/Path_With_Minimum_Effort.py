
from typing import List
from heapq import heappush, heappop

'''

[[1,2,2],
 [3,8,2],
 [5,3,5]]
 
'''
class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        destination = [rows - 1, columns - 1]
        
        p_queue = []
        ROWS, COLS = rows, columns
        heappush(p_queue,[0, [0, 0]])
        
        distance = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]
        distance[0][0] = 0
        
        while p_queue:
            curr_distance_cost, pos = heappop(p_queue)
            
            if pos == destination:
                return curr_distance_cost
                
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            row , col = pos
            
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    new_distance_cost = max(curr_distance_cost, min(distance[new_row][new_col], abs(heights[row][col] - heights[new_row][new_col])))

                    if new_distance_cost < distance[new_row][new_col]:
                        distance[new_row][new_col] = new_distance_cost
                        heappush(p_queue, [new_distance_cost, [new_row, new_col]])
                    
        return -1



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

        print("~")
# } Driver Code Ends