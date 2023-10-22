class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #construct graph ~ adjency list
        graph = {}
        visited, components = set(), 0 
        
        for i in range(n):
            graph[i] = []
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        def dfs(node):
            if node in visited: return
            
            visited.add(node)
            
            for nei in graph[node]:
                dfs(nei)
                
        for n in graph:
            if n not in visited:
                components += 1
                dfs(n)
                
        return components
    
    
    
    # Time = O(n + m)
    # Space = O(n + m)