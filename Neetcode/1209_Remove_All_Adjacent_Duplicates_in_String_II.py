#Brute Force
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #create a set of potential duplicates 
        duplicates = { k*c for c in ascii_lowercase}

        #replace duplicates with "" in s as long as they exist
        prev_len = 0

        while prev_len != len(s):
            prev_len = len(s)
            for dup in duplicates:
                s = s.replace(dup, "")

        return s

        # TC: O(n^2)
        # SC: O(n)

#Optimal - Using a stack
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_stack = []
        count_stack = []

        for c in s:
            if not char_stack or char_stack[-1] != c:
                char_stack.append(c)
                count_stack.append(1)
                continue
            char_stack.append(c)
            count_stack[-1] += 1

            if count_stack[-1] == k:
                for i in range(k):
                    char_stack.pop()
                count_stack.pop()

        return "".join(char_stack)

        # TC: O(n*k)
        # SC: O(n)