class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        table = {}

        for p in range(1, n + 1):
            table[p] = 0

        for a, b in trust:
            table[a] -= 1
            table[b] += 1

        for key in table.keys():
            if table[key] == n - 1:
                return key
        return -1
        
# Time = O(n + m) |Vertices| + |Edges|
# Space = O(n)


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        connections = [0] * (n + 1)

        for v in trust:
            connections[v[0]] -= 1
            connections[v[1]] += 1

        for i in range(1, n + 1):
            if connections[i] == n - 1:
                return i

        return -1
