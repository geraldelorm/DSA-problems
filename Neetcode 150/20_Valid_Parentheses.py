class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"(":")", "{":"}", "[":"]"}
        stack = collections.deque()
        
        for p in s:
            if p in paren:
                stack.append(p)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if ((p == ")" and top != "(") or
                    (p == "}" and top != "{") or
                    (p == "]" and top != "[")):
                    return False
                
        return not stack
    
    # TC: O(N)
    # SC: O(N)