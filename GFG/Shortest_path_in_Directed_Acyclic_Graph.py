#User function Template for python3

from typing import List
import collections

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
                         
        #create graph
        graph = collections.defaultdict(list)

        for fro, to, dist in edges:
            graph[fro].append([to, dist])

        #create topo ordering
        visited = set() #just this cos there are no cycles
        topo_order_stack = []
        
        def dfs(curr_v): #simple cos there are not cycles to check for
            visited.add(curr_v)
            
            for next_v, dist in graph[curr_v]:
                if next_v not in visited:
                    dfs(next_v)
                
            topo_order_stack.append(curr_v)

        for v in range(V):
            if v not in visited:
                dfs(v)
                
        # Pop from topo stacck and relax edges - distance update
        distance = [float("inf")] * V
        distance[0] = 0 #mark distance to source

        while topo_order_stack:
            curr_v = topo_order_stack.pop()
            curr_dist = distance[curr_v]
            
            for next_v, next_dist in graph[curr_v]:
                if curr_dist + next_dist < distance[next_v]:
                    distance[next_v] = curr_dist + next_dist

        for i, d in enumerate(distance):
            if d == float("inf"):
                distance[i] = -1
                
        return distance
                
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List


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


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        edges = IntMatrix().Input(m, 3)

        obj = Solution()
        res = obj.shortestPath(n, m, edges)

        IntArray().Print(res)
        print("~")

# } Driver Code Ends