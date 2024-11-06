#User function Template for python3
from typing import List
import collections

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        indegree = collections.defaultdict(set)
        
        for node, edges in enumerate(adj):
            for edge in edges:
                indegree[edge].add(node)
                
        queue = collections.deque()
        
        for node in range(V):
            if not indegree[node]:
                queue.append(node)
                
        topo_order = []
        
        while queue:
            curr_node = queue.popleft()
            topo_order.append(curr_node)
            
            for edge in adj[curr_node]:
                indegree[edge].remove(curr_node)
                
                if not indegree[edge]:
                    queue.append(edge)
                    
        if len(topo_order) == V:
            return 0
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

        print("~")
# } Driver Code Ends