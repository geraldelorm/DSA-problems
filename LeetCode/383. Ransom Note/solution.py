class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lookup = {}
        for c in magazine:
            if c in lookup:
                lookup[c] += 1
            else:
                lookup[c] = 1
                        
        for c in ransomNote:
            if not c in lookup or lookup[c] <= 0:
                return False
            else:
                lookup[c] -= 1
        return True


# Time = o(n)
# Space = O(n)