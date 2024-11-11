from typing import List
from heapq import heappush, heappop
import collections

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        queue = collections.deque()
        queue.append([0, start])
        
        distance = [float("inf")] * 100000
        distance[start] = 0
        
        while queue:
            num_of_mult, curr_pos = queue.popleft()
            
            if curr_pos == end:
                return num_of_mult
                
            for multiplier in arr:
                new_pos = (curr_pos * multiplier) % 100000
                
                if distance[new_pos] > num_of_mult + 1:
                    distance[new_pos] = num_of_mult + 1
                    
                    queue.append([num_of_mult + 1, new_pos])
                    
        return -1
        
