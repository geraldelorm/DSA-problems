class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        nums.sort()
        longest = 1
        curr_max = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_max += 1
                else:
                    longest = max(longest, curr_max)
                    curr_max = 1

        return max(longest,curr_max)

        # TC: O(nlogn)
        # SC: O(1)
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                curr_max = 1
                curr_num = num
                while curr_num + 1 in nums_set:
                    curr_max += 1
                    curr_num += 1
                
                longest = max(longest,curr_max)
                

        return longest

        # TC: O(n)
        # SC: O(n)