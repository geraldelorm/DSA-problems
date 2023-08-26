class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def search(sub):
            if sub in memo:
                return memo[sub]

            res = []

            #recursion
            for i in range(len(sub)):
                prefix = sub[:i + 1]

                if prefix in words:
                    if prefix == sub:
                        res.append(prefix)
                    else:
                        for phrase in search(sub[i + 1:]):
                            res.append(prefix + " " + phrase)

            memo[sub] = res
            return res

        return search(s)
        