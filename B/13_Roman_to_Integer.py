class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        look_up = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M":1000}
        deductable = {"I": {"V", "X"}, "X" : {"L", "C"}, "C": {"D", "M"}}

        for i, c in enumerate(s):
            val = look_up[c]
            if c in deductable and i < len(s) - 1 and s[i + 1] in deductable[c]:
                res -= 2 * look_up[c]
            res += val

        return res

# TC: O(n)
# SC: O(1)