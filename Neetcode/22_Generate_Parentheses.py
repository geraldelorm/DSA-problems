#Generate All posible parenthesis and check thier validity
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def isValid(s):
            openerCount = 0

            for c in s:
                if c == "(":
                    openerCount += 1
                else:
                    openerCount -= 1
                if openerCount < 0:
                    return False

            return openerCount == 0

        def generate(parenthesis):
            if len(parenthesis) == 2*n:
                if isValid(parenthesis):
                    res.append(parenthesis)
                return
            
            generate(parenthesis + "(")
            generate(parenthesis + ")")

        generate("")
        return res

        # TC: O(2^2n * n) 
        # 2n calls recursive calls where 2 choices are made on each itration and n to check validity
        # SC: O(2^2n * n)


# Using backtracking and checking validity as we build the potential perenthesis
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(parenthesis, open_count, close_count):
            if len(parenthesis) == 2*n:
                result.append("".join(parenthesis))
                return
            if open_count < n:
                parenthesis.append("(")
                generate(parenthesis, open_count + 1, close_count)
                parenthesis.pop()
            if open_count > close_count:
                parenthesis.append(")")
                generate(parenthesis, open_count, close_count  + 1)
                parenthesis.pop()

        generate([], 0, 0)
        return result