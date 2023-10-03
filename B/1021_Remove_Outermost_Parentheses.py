''' 
Input -> Output:
None -> ""
""  -> ""
"()" -> ""
"(())" -> "()"
"()()()" -> "()"
"((()))(())()()((()))" -> "(())()(())"


stack = []
output = ["(())", ]
currSection = ""

Approach:
Go over the input string for each character:
    add opener to a stack
    for closer 
    if stack_len > 1:
        pop from the stack and add the pair to curr section
    if stack_len == 1:
        just pop and inidicate the start of a new segment
    
'''


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = []
        count = 0

        for c in s:
            if c == "(":
                if count >= 1:
                    output.append(c)
                count += 1
            else:
                if count > 1:
                    output.append(c)
                count -= 1

        return "".join(output)

        # TC: O(n)
        # SC: O(n)