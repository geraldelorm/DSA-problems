class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []

        p_map, s_map = collections.Counter(p), {}
        left, res = 0, []

        for right in range(len(s)):
            s_map[s[right]] = s_map.get(s[right], 0) + 1

            if right - left + 1 == len(p):
                if self.isAnagram(p_map, s_map):
                    res.append(left)

                s_map[s[left]] -= 1
                left += 1

        return res
            
    def isAnagram(self, p_map, s_map):
        for k in p_map:
            if k not in s_map:
                return False
            if s_map[k] != p_map[k]:
                return False

        return True

    # TC: O(n + m)
    # SC: O(K) ~ k == 26


        
        