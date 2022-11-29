class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for f, t, p in times:
            edges[f].append((t, p))

        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            c_time, c_node = heapq.heappop(minHeap)

            if c_node in visited:
                continue

            visited.add(c_node)
            time = max(time, c_time)

            for n_node, n_time in edges[c_node]:
                if n_node not in visited:
                    heapq.heappush(minHeap, (c_time + n_time, n_node))

        print(visited)
        return time if len(visited) == n else -1


#         O(E * LogV); E = edges, V = vertex
