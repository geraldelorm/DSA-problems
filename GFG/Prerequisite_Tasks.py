#User function Template for python3
import collections 

class Solution:
    def isPossible(self,N,P,prerequisites):
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
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
        print("~")
# } Driver Code Ends