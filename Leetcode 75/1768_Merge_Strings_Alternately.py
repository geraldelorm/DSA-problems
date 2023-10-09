class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = []
        i = j = 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
                i += 1
            if j < len(word2):
                res.append(word2[j])
                j += 1

        return "".join(res)

# TC: O(n)
# SC: O(n) result array
