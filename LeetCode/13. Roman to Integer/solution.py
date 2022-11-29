class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        for i in range(len(s)):
            if i + 1 < len(s) and lookup[s[i]] < lookup[s[i +1]]:                    
                count -= lookup[s[i]]
            else:
                count += lookup[s[i]]
        return count


# Time = o(n)
# Space = O(1) lookup table