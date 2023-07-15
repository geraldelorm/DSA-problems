class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start, end, all_paths = 0, len(graph) - 1, []
        
        queue = collections.deque([[0]]) #starting path with [startNode]
        
        while queue:
            path = queue.popleft()
            
            if path[-1] == end:
                all_paths.append(path)
                
            for n in graph[path[-1]]:
                queue.append(path + [n])
                
        return all_paths
    
    
#     Time = O(2^N . N)
#     Space = O(2^N . N)