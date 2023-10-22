class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

# Space = O(n)
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None: # Space = O(n); Time = O(n) : where n = char in word
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool: # Space = O(1); Time = O(n) : where n = char in word
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool: # Space = O(1); Time = O(n) : where n = char in word
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)