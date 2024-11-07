#User function Template for python3
import collections 

class Solution:
    def shortestPath(self, edges, n, m, src):
        graph = collections.defaultdict(set)
        
        for fro, to in edges:
            graph[fro].add(to)
            graph[to].add(fro)
            
            
        queue = collections.deque()
        queue.append([src, 0])
        distance = [float("inf")] * n
        visited = set()
        visited.add(src)
        
        while queue:
            curr_v, dist = queue.popleft()
            distance[curr_v] = dist
            
            for next_v in graph[curr_v]:
                if next_v not in visited:
                    visited.add(next_v)
                    queue.append([next_v, dist + 1])
                    
        for i, d in enumerate(distance):
            if d == float("inf"):
                distance[i] = -1
                
        return distance
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends