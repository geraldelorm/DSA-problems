from collections import deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        graph = {}

        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]

        queue, visited = deque(), set()
        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            if node == end:
                return True

            for adjacent_node in graph[node]:
                if adjacent_node not in visited:
                    queue.append(adjacent_node)
                    visited.add(adjacent_node)

        return False

# Time = O(n + m) |Vertices| + |Edges|
# Space = O(n)
