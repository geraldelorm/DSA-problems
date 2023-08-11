class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a bucket
        res = []
        seen = set()
        
        def isAnagram(s1, s2):
            return sorted(s1) == sorted(s2)
        
        #iterate over the input:
        for i, _str in enumerate(strs):
            if _str not in seen:
                ana = [_str]
                #for each string find all anagrams present in the input
                for j in range(i + 1, len(strs)):
                    if isAnagram(_str, strs[j]):
                        ana.append(strs[j])
                        seen.add(strs[j])
                seen.add(_str)
                #update my backet
                res.append(ana)
                
        # return the bucket
        return res
                
        # TC: O(n^2*slogs)
        # SC: O(n)
        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        def getKey(s):
            key = 0
            for c in s:
                key += ord(c)
                
            return key 
        
        for i, _str in enumerate(strs):
            key = tuple((sorted(_str)))
            anagrams[key].append(_str)
                
        return anagrams.values()
                
        # TC: O(n*slogs)
        # SC: O(ns)
        
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        def getKey(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            return tuple(count)
        
        for i, _str in enumerate(strs):
            key = getKey(_str)
            anagrams[key].append(_str)
                
        return anagrams.values()
                
        # TC: O(n*)
        # SC: O(ns)