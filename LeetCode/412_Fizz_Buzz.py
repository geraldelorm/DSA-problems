class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * n

        for i in range(n):
            curr_n = i + 1
            if not curr_n % 3 and not curr_n % 5:
                res[i] = "FizzBuzz"
            elif not curr_n % 3:
                res[i] = "Fizz"
            elif not curr_n % 5:
                res[i] = "Buzz"
            else:
                res[i] = str(curr_n)

        return res

    # TC: O(N)
    # SC: O(N)