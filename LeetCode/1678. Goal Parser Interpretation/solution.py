class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        for s in range(len(command)):
            if command[s] == "G":
                output += "G"
            elif command[s] == "(":
                if command[s + 1] == ")":
                    output += "o"
                elif command[s + 1] == "a":
                    output += "al"     
        return output

# Time Complexity = O(n)
# Space Complexity = O(n)