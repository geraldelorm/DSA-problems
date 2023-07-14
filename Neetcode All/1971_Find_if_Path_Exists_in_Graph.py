class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # construct graph - adjacency list
        graph = collections.defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        # do a traversal to find the destination starting from the source
        
        visited = [False] * n
        queue = collections.deque()
        queue.append(source)
        visited[source] = True
        
        while queue:
            curr = queue.popleft()
            
            if curr == destination:
                return True
            
            for node in graph[curr]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    
        return False

    # Time = O(n + m) vertices + edges
    # space = O(n) number of nodes in the graph