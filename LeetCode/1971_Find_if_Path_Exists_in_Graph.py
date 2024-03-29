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


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #BFS
        graph = {}

        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]

            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]

        visited = set()
        tovisit = deque()
        tovisit.append(source)

        while len(tovisit):
            curr = tovisit.popleft()

            if curr == destination:
                return True

            visited.add(curr)

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    tovisit.append(neighbour)

        return False
