class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        look_up = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for i, c in enumerate(s):
            if i < len(s) - 1 and look_up[s[i + 1]] > look_up[c]:
                res -= look_up[c]
            else:
                res += look_up[c]
        return res
    
# Time = O(n) - if input is condisered as a string with characters that are travesed
# Space = O(1)