#User function Template for python3
import collections 

class Solution:
    def findOrder(self, N, m, prerequisites):
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(set)
        
        for course, prereq in prerequisites:
            indegree[course].add(prereq)
            graph[prereq].add(course)
            
        queue = collections.deque()
            
        for course in range(N):
            if not indegree[course]:
                queue.append(course)
                
        topo_order = []

        while queue:
            curr_course = queue.popleft()
            topo_order.append(curr_course)

            for next_course in graph[curr_course]:
                indegree[next_course].remove(curr_course)
                if not indegree[next_course]:
                    queue.append(next_course)
                    
                    
        if len(topo_order) == N:
            return topo_order
        else:
            return []


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
        print("~")
# } Driver Code Ends