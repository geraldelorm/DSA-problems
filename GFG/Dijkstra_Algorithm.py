#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
import heapq
from typing import List, Tuple


# } Driver Code Ends

import collections 
import heapq

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        for node in range(len(adj)):
            for next_node, cost in adj[node]:
                graph[node].append([next_node, cost])
        
        distance = [float("inf")] * len(adj)
        distance[src] = 0
        
        p_queue = []
        
        heapq.heappush(p_queue, [0, src])
        
        while p_queue:
            curr_dist, curr_node = heapq.heappop(p_queue)
            
            for next_node, next_dist in graph[curr_node]:
                if curr_dist + next_dist < distance[next_node]:
                    distance[next_node] = curr_dist + next_dist
                    heapq.heappush(p_queue, [curr_dist + next_dist, next_node])
                    
                    
        return distance
        
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        src = int(input())
        ob = Solution()

        res = ob.dijkstra(adj, src)
        for i in res:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends