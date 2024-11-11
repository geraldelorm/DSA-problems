from typing import List
import collections
from heapq import heappush, heappop
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
       
        for start, end, cost in roads:
            graph[start].append([end, cost])
            graph[end].append([start, cost])
            
        p_queue = []
        heappush(p_queue, [0, 0])
        
        distance = [float("inf")] * n
        distance[0] = 0
        
        ways = [0] * n
        ways[0] = 1
        
        
        while p_queue:
            curr_cost, pos = heappop(p_queue)
            
            for next_pos, next_cost in graph[pos]:
                if curr_cost + next_cost < distance[next_pos]:
                    distance[next_pos] = curr_cost + next_cost
                    heappush(p_queue, [curr_cost + next_cost, next_pos])
                    ways[next_pos] = ways[pos]
                    
                elif curr_cost + next_cost == distance[next_pos]:
                    ways[next_pos] = (ways[next_pos] + ways[pos]) % ((10**9) + 7)
                
        
        return ways[n - 1] % ((10**9) + 7)
        

