# Naive Solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ""
        for c in address:
            if c == ".":
                new_address += "[.]"
            else:
                new_address += c
        return new_address

# Optimal Solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

# Time Complexity = O(n)
# Space Complexity = O(n)