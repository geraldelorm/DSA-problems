class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                to_decode = ""
                while stack and stack[-1] != "[":
                    to_decode = stack.pop() + to_decode

                stack.pop() #remove the "[" bofore multiplier

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(to_decode * int(multiplier))

        return "".join(stack)

        # TC: O(n * maxK^countofK)
        # SC: O(sum(n * maxK^countofK)))
                
