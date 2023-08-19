class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "{":"}", "[":"]"}

        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if pairs[top] != c:
                    return False

        return not stack

# TC: O(n)
# SC: O(n)
        