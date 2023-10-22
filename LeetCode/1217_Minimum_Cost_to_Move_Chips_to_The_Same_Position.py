class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_positions, odd_positions = 0, 0

        for pos in position:
            if pos % 2:
                even_positions += 1
            else:
                odd_positions += 1

        return min(even_positions, odd_positions)

# TC: O(n)
# SC: O(1)