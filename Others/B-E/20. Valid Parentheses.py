# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# E.G
# "()" = true
# "()[]{}" = true
# "(()" = false
# "[{}()]" = true
# "[{)(}]" = False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()

        for c in s:
            if c in set(("(", "[", "{")):
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                op = stack.pop()
                if op == "(" and c != ")":
                    return False
                if op == "[" and c != "]":
                    return False
                if op == "{" and c != "}":
                    return False

        return len(stack) == 0


# Space = O(n)
# Time = O(n)

# Clean Code
class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        pairs = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pairs.keys():
                if stack and stack.pop() == pairs[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
