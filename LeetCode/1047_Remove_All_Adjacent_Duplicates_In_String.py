#Brute Force
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        #create a set of duplicates 
        duplicates = {2*c for c in ascii_lowercase}

        #while s contains duplicates replace them with ""
        prev_len = 0
        while prev_len != len(s):
            prev_len = len(s)
            for dup in duplicates:
                s = s.replace(dup, "")

        return s

        # TC: O(N^2)
        # SC: O(N)

#Optimal
class Solution:
    def removeDuplicates(self, s: str) -> str:
        #track the characters in a stack 
        stack = [] 

        #iterate over s if the curr char == top of stack then I can pop from the stack
    
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
                continue
            stack.append(c)

        return "".join(stack)

        # TC: O(N)
        # SC: O(N) O(1) if result is not considered 