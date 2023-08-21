class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def validParenthessis(parathesis):
            left_count = 0

            for p in parathesis:
                if p == "(":
                    left_count += 1
                elif not left_count:
                    return False
                else:
                    left_count -= 1

            return not left_count

        def create(parenthesis, open_count, close_count):
            if open_count + close_count == 2 * n:
                if validParenthessis(parenthesis):
                    res.append("".join(parenthesis))
                return

            create(parenthesis + ["("], open_count + 1, close_count)
            create(parenthesis + [")"], open_count , close_count + 1)


        create([], 0, 0)
        return res

    # TC: O((2^2*n)*n)
    # SC: O((2^2*n)*n)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(parenthesis, open_count, close_count):
            if open_count + close_count == 2 * n:
                res.append("".join(parenthesis))
                return
            if open_count < n:
                parenthesis.append("(")
                backtracking(parenthesis, open_count + 1, close_count)
                parenthesis.pop()
            if close_count < open_count:
                parenthesis.append(")")
                backtracking(parenthesis, open_count , close_count + 1)
                parenthesis.pop()

        backtracking([], 0, 0)
        return res

    # TC: O(4^n/sptr(n))
    # SC: O(n)
        