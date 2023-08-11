class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:    
        safe_nodes = []
        state = {} 
        
        def isSafe(node): 
            if node in state:
                return state[node]
            
            state[node] = False
            
            for nei in graph[node]:
                if not isSafe(nei):
                    return False
                
            state[node] = True
            return True
        
        for n in range(len(graph)): 
            if isSafe(n):
                safe_nodes.append(n)
        
        return safe_nodes
    
    # Time = O(N + M)
    # Space = O(N)
