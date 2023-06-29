class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set()
        longest_consecutive = 0
        
        for n in nums:
            lookup.add(n)
            
        for n in lookup:
            if (n - 1 not in lookup):
                curr_number = n
                curr_longest_consecutive = 1
                
                while curr_number + 1 in lookup:
                    curr_number += 1
                    curr_longest_consecutive += 1 
                
                longest_consecutive = max(longest_consecutive, curr_longest_consecutive)
                
        return longest_consecutive
    
    
# Time = O(n)
# Space = O(n)