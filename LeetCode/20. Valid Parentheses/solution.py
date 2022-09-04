class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
                
            elif not len(stack): return False
            
            else:
                if c == ')' and stack.pop() != '(': return False
                elif c == '}' and stack.pop() != '{': return False
                elif c == ']' and stack.pop() != '[': return False
        return not len(stack)


# Time Complexity = O(n)
# Space Complexity = O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c in ["(", "{", "["]:
                stack.appendleft(c)
            elif len(stack) < 1:
                return False
            else:
                if c == ")" and stack.popleft() != "(":
                    return False
                if c == "]" and stack.popleft() != "[":
                    return False
                if c == "}" and stack.popleft() != "{":
                    return False

        return len(stack) == 0

#   Time O(n)
#   Space O(n)
