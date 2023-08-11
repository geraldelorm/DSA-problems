class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        def operate(val1, val2, operation):
            match operation:
                case "+":
                    return val1 + val2
                case "-":
                    return val1 - val2
                case "*":
                    return val1 * val2
                case "/":
                    return int(val1 / val2)

        for token in tokens:
            if token in operators:
                val2 =  stack.pop()
                val1 = stack.pop()
                res = operate(val1, val2, token)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()

        # TC: O(n)
        # SC: O(n)