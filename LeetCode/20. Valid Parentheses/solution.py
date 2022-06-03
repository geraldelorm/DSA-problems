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