class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if v + numbers[j] == target:
                    return [i +1, j + 1]
    # TC: O(n^2)
    # SC: O(1)

            
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(numbers):
            diff = target - v
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            seen[v] = i

    # TC: O(n)
    # SC: O(n)
    
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            else:
                left += 1

    # TC: O(n)
    # SC: O(1)