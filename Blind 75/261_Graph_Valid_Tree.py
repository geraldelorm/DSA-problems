class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #construct the graph using 
        graph = collections.defaultdict(list, {i: [] for i in range(n)})
        visited, connected_components = set(), 0
        
        
        for source, des in edges:
            graph[source].append(des)
            graph[des].append(source)
            
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            
            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True
        
            
        return dfs(0, -1) and len(visited) == n
    
    # Time = O(n + m)
    # Space = O(n + m)