#Brute Force - replace diplicates in string
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        #generate all possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        #use lenght to track is S changed
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for dup in duplicates:
                s = s.replace(dup, "")

        return s
        # TC: O(N^2)
        # SC: O(n)

#Optimal Solution - using a output stack to
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []

        for c in s:
            if output and c == output[-1]:
                output.pop()
            else:
                output.append(c)

        return "".join(output)
        # TC: O(n)
        # SC: O(n)