#Brute Force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            output.append(product)

        return output

        # TC: O(n^2)
        # SC: O(n) ~ output included


#Using postfix and prefix product arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * (len(nums) + 1), [1] * (len(nums) + 1)

        for i in range(1, len(left)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(right) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]

        for i in range(1, len(right)):
            nums[i - 1] = (left[i - 1] * right[i])

        return nums


        # TC: O(n)
        # SC: O(n) ~ output not included


#Most Optimal ~ use one array which will be return
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        last_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * last_product
            last_product = last_product * nums[i]

        return answer


        # TC: O(n)
        # SC: O(1) ~ output not included