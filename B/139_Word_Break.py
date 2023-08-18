class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        def search(s, memo):
            if s in memo: return memo[s]
            if len(s) == 0:
                return True

            for i in range(1, len(s) + 1):
                memo[s] = s[:i] in word_dict and search(s[i:], memo)
                if memo[s]:
                    return True

            return False
        return search(s, {})

        # TC: O(n^2 * k * w )
        # SC: O(w + s )


# Better DP - Top down
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        @cache
        def search(i):
            if i < 0: return True

            for word in wordDict:
                if word == s[i - len(word) + 1: i + 1] and search(i - len(word)):
                    return True

            return False
        return search(len(s) - 1)

        # TC: O(s * k * w)
        # SC: O(s)