#User function Template for python3
from typing import List
import collections
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        graph = collections.defaultdict(list)

        for node, next_node, cost in edges:
            graph[node].append([next_node, cost])
            graph[next_node].append([node, cost])
        
        distance = [float("inf")] * (n + 1)
        parent = [-1] * (n + 1)
            
        p_queue = []
        heapq.heappush(p_queue, (0, 1, -1))
        
        while p_queue:
            curr_dist, curr_node, parent_node = heapq.heappop(p_queue)
            
            if curr_dist > distance[curr_node]:
                continue
            
            distance[curr_node] = curr_dist
            parent[curr_node] = parent_node
            
            for next_node, next_dist in graph[curr_node]:
                if curr_dist + next_dist < distance[next_node]:
                    distance[next_node] = curr_dist + next_dist
                    heapq.heappush(p_queue, (curr_dist + next_dist, next_node, curr_node))

        
        if distance[n] == float("inf"): return [-1]
        
        path = []
        node = n
        
        while node != -1:
            path.append(node)
            node = parent[node]
            
        path.append(distance[n])
        path.reverse()
        return path
        