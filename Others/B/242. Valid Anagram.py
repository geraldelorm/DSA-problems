# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# E.G
# s = "car" t= "rac" : true
# s = "anagram", t = "nagaram" : ture
# s = gam t = mag: true
# s = book t= cook: false

# Brute Force
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

# Time = O(NlogN)
# Spave = O(1) - if sorting is done inplace


# Better Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_map, s_map = {}, {}

        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1
            s_map[s[i]] = s_map.get(s[i], 0) + 1

        for k in t_map:
            if k not in s_map or s_map[k] != t_map[k]:
                return False

        return True

# Time = O(N)
# Spave = O(N)


# Best Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0] * 26 #ask if charactes=rs are ascii

        for c in s:
            idx = ord(c) - ord("a")
            arr[idx] += 1

        for c in t:
            idx = ord(c) - ord("a")
            arr[idx] -= 1

        for v in arr:
            if v != 0:
                return False

        return True

# Time = O(N)
# Space = O(1) - 26 char array set


# What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# Use a hash_map instead of array if it is not ascii characters but unicode