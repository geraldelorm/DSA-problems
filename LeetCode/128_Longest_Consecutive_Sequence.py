# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) < 1: return 0
#         nums.sort()
#         max_sequence, curr_max = 1, 1

#         for i in range(1, len(nums)):
#             if nums[i - 1] != nums[i]:
#                 if nums[i - 1] + 1 == nums[i]:
#                     curr_max += 1
#                 else:
#                     max_sequence = max(max_sequence, curr_max)
#                     curr_max = 1

#         return max(max_sequence, curr_max)

# Time = O(nlogn)
# Space = O(1) -> if sorting is done inplace

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_squence = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_squence += 1

                max_sequence = max(max_sequence, curr_squence)

        return max_sequence

        # Time = O(n)
        # Space = O(n)
