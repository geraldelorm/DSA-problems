class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])

        half = len(costs) // 2
        total = 0
        for i in range(half):
            total += costs[i][0]

        for i in range(half, len(costs)):
            total += costs[i][1]

        return total

    # TC: O(NlogN)
    # SC: O(1) we only modify the original list