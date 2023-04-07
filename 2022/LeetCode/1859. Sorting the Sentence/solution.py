class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        lookup = {}
        
        for word in words:
            lookup[int(word[-1])] = word[:-1]
            
        return " ".join([lookup[i + 1] for i in range(len(lookup))])


# TIme O(n)
# Space O(n)