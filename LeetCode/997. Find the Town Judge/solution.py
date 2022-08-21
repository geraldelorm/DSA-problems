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
