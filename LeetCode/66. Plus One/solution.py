class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #         num = ""
        #         for i in range(len(digits)):
        #             num = num + str(digits[i])

        #         num = int(num) + 1
        #         output = []

        #         for c in str(num):
        #             output.append(c)

        #         return output

        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits

# O(N) - time - len of digits
# O(N) - space - we create string and a results array
