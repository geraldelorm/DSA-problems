class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        place_value = 1

        for i in range(len(columnTitle) - 1, -1, -1):
            val = ord(columnTitle[i]) - ord("A") + 1
            position_val = val * place_value
            column_number += position_val
            place_value *= 26

        return column_number

# TC: O(N)
# SC: O(1)