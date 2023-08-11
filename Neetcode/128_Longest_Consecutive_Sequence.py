#With sorting ~ not optimal
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        curr_consecutives = 1
        longest_consecutives = 1
        
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]: 
                if nums[i] == nums[i + 1] - 1:
                    curr_consecutives += 1
                else:
                    longest_consecutives = max(longest_consecutives, curr_consecutives)
                    curr_consecutives = 1

        return max(longest_consecutives, curr_consecutives)
    
    # TC: O(nlogn)
    # SC: O(1)
    
    
    
#Clever Optimal Solution ~ using a table table to figue out increments
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutives = 0
        
        for num in nums_set:
            if num - 1 not in nums_set: #check if we have done this in the passs starting from smallest
                curr_num = num
                curr_consecutives = 1
                
                while curr_num + 1 in nums_set:
                    curr_consecutives += 1
                    curr_num += 1
                    
                longest_consecutives = max(longest_consecutives, curr_consecutives)
                
        return longest_consecutives
    
    # TC: O(n)
    # SC: O(n)
    
