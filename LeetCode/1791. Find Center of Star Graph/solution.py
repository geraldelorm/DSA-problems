class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        table = {}

        for i in range(len(edges)):
            if edges[i][0] in table:
                table[edges[i][0]] += 1
            else:
                table[edges[i][0]] = 1

            if edges[i][1] in table:
                table[edges[i][1]] += 1
            else:
                table[edges[i][1]] = 1

        for key in table.keys():
            if table[key] == len(edges):
                return key


# Time = O(n + m) |Vertices| + |Edges|
# Space = O(n)


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = [0] * (len(edges) + 2)

        for v in edges:
            connections[v[0]] += 1
            connections[v[1]] += 1

        for i in range(1, len(connections)):
            if connections[i] == len(edges):
                return i
