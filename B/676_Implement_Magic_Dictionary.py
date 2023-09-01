class MagicDictionary:

    def __init__(self):
        self.words = set()
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        

    def search(self, searchWord: str) -> bool:

        for word in self.words:
            if len(word) == len(searchWord):
                requiredChanges = 0
                for i in range(len(word)):
                    if word[i] != searchWord[i]:
                        requiredChanges += 1
                
                if requiredChanges == 1:
                    return True
        return False

    # TC: O(ns) n = no. words; s = len(word)
    # SC: O(n)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


#Improve this a bit by storing word with the same length in ane bucket 