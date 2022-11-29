# class Solution:
#     def countGoodSubstrings(self, s: str) -> int:
#         if len(s) < 3:
#             return 0
#         size, good, l= 3, 0, 0
#         lookup = {}

#         for i in range(size):
#             lookup[s[i]] = lookup.get(s[i], 0) + 1

#         if len(lookup) == 3: good += 1

#         for r in range(size, len(s)):
#             lookup[s[r]] = lookup.get(s[r], 0) + 1
#             lookup[s[l]] -= 1
#             if lookup[s[l]] == 0:
#                 del lookup[s[l]]

#             if len(lookup) == 3: good += 1


#             l += 1

#         return good


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        count = 0
        k = 3
        while right < len(s):
            if right - left + 1 == k:
                if s[right] != s[right - 1] and s[right] != s[right - 2] and s[right - 1] != s[right - 2]:
                    count += 1
                left += 1

            right += 1

        return count