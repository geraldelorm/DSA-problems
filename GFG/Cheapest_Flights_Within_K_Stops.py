#User function Template for python3
from typing import List
import collections
from heapq import heappush, heappop

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        graph = collections.defaultdict(list)
        
        for source, destination, cost in flights:
            graph[source].append([destination, cost])
            
        min_cost = float("inf")
        
        p_queue = []
        heappush(p_queue, [0, src, 0])
        distance = [float("inf")] * n
        distance[src] = 0
        
        while p_queue:
            stops, curr_pos, curr_cost = heappop(p_queue)

            if curr_pos == dst:
                min_cost = min(min_cost, curr_cost)
                continue
                
            if stops > k:
                continue
            
            for next_pos, next_cost in graph[curr_pos]:
                if distance[next_pos] > curr_cost + next_cost:
                    distance[next_pos] = curr_cost + next_cost
                    heappush(p_queue, [stops + 1, next_pos, curr_cost + next_cost])
          
        return min_cost if min_cost != float("inf") else -1
                
