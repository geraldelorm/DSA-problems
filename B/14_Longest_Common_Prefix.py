#There are a lot of possible solutions 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        prefix = strs[0]

        for word in strs:
            while len(prefix) > len(word) or prefix != word[:len(prefix)]:
                prefix = prefix[:len(prefix) - 1]

                if prefix == "":
                    return prefix

        return prefix

# TC:O(S(len(word)))
# SC: O(len(word))


#Try Solving with Binary search and Trie

