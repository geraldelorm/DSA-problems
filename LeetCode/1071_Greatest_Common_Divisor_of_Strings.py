#Brute Force
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        l1, l2 = len(str1) , len(str2)

        def valid_gcd(k):
            if l1 % k or l2 % k: #if the range if not divisible by both string len
                return False

            str1_sub_strings, str2_sub_strings = l1 // k, l2 // k
            common_sub_string = str1[:k]

            return str1 == common_sub_string * str1_sub_strings and str2 == common_sub_string * str2_sub_strings

        for i in range(min(l1, l2), 0, -1):
            if valid_gcd(i):
                return str1[:i]

        return ""
        
# TC: O(min(s1, s2) * (s1 + s2))
# SC: O(min(s1, s2))
        

import math

# Optimal
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # check if a gcd range exist
        if str1 + str2 != str2 + str1:
            return ""

        gcd_range = math.gcd(len(str1), len(str2))
        return str1[:gcd_range]

# TC: O(s1 + s2)
# SC: O(s1 + s2)