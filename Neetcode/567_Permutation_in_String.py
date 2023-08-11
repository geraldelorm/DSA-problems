class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1: return True
        if len(s1) > len(s2): return False
        
        s1_count, s2_count = {}, {}
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

            
        for i in range(len(s1), len(s2)):
            if s1_count == s2_count: #O(26) ~ comparing maps
                return True

            #move window buy removing let element from map and adding right element
            s2_count[s2[i - len(s1)]] -= 1
            if s2_count[s2[i - len(s1)]] == 0:
                del s2_count[s2[i - len(s1)]]
                
            #update with right value
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            
    
        #after full iteration compare if maps are equal in the end
        return s1_count == s2_count
    
    # TC: O(n * 26)
    # SC: O(n)
    
    
#Slight improvement by avoiding map comparism 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
    # TC: O(n)
    # SC:O(n)