class Solution:
    # def isAnagram(self, map1, map2):
    #     for k in map1:
    #         if k not in map2:
    #             return False
    #         if map1[k]  != map2[k]:
    #             return False
    #     return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_map, s_map, res = {}, {}, []

        for i in range(len(p)):
            p_map[p[i]] = p_map.get(p[i], 0) + 1
            s_map[s[i]] = s_map.get(s[i], 0) + 1

        if p_map == s_map:
            res.append(0)

        l = 0
        for r in range(len(p), len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            s_map[s[l]] -= 1

            if s_map[s[l]] == 0:
                s_map.pop(s[l])

            if p_map == s_map:
                res.append(l + 1)

            l += 1

        return res


#     Time O(S)
