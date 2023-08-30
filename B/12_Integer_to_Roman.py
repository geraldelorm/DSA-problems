class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_to_val = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        res = ""

        for symbol in symbol_to_val:
            while num >= symbol_to_val[symbol]:
                res += symbol
                num -= symbol_to_val[symbol]


        return res

    # TC: O(1)
    # SC: O(1)
