class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = {i: 0 for i in range(1, n + 1)}

        for [p1, p2] in trust:
            degrees[p1] += 1
            degrees[p2] -= 1

        for person in range(1, n +1):
            if degrees[person] == -n + 1:
                return person

        return -1

        # TC: O(E) edges
        # SC: O(N) 