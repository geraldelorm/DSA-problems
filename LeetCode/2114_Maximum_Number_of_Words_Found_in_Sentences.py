from ast import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for s in sentences:
            words = s.split(" ")
            if len(words) > max:
                max = len(words)
        return max

# Time Complexity = O(n)
# Space Complexity = O(n)