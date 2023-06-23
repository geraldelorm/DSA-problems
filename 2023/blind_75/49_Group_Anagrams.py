from collections import defaultdict 

#Using a hashmap with sorted string/tuple as key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            d[sorted_s].append(s)
            
        return [v for v in d.values()]
    
# Time = O(NSlogS) where N is the len(of list) and S is len(longest string in list)
# Space = O(NS) hashmap of array of anagrams


#Using a hashmap with tuple count of characters as key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            d[tuple(count)].append(s)
            
        return d.values()
    
    
# # Time = O(NS)
# # Space = O(NS)