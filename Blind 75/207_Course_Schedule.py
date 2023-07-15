class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct the graph - adjacency list
        graph = {}

        for course, pre in prerequisites:
            if course not in graph:
                graph[course] = {
                    'canTake': False, 
                    'visited' : False, 
                    'preReqs' : [pre]
                }
            else:
                graph[course]['preReqs'].append(pre)
                
        print(graph)
                        
        # traverse and dertermine if the graph has a cyclic dependancy
        def dfs(course):
            #course has no preReq
            if course not in graph: 
                return True 
            
            #all preReqs have been taken 
            if graph[course]['canTake']:
                return True 
            
            #course has another dependancy #therefore can't complete ~ cycle detected
            if graph[course]['visited']:
                return False 
            
            graph[course]['visited'] = True
            
            for preReq in graph[course]['preReqs']:
                if not dfs(preReq): return False
            
            # canTake cos all preReqs reurned True
            graph[course]['canTake'] = True
            return True
        
        # do cycle check on all courses
        for c in range(1, numCourses):
            if not dfs(c): return False
            
        return True
    
    # Time = O(n + m)
    # Space = o(n + m)