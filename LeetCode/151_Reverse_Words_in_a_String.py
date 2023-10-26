class Solution:
    def reverseWords(self, s: str) -> str:
        words_stack = []
        curr_word = []

        for i, c in enumerate(s):
            if c == " ":
                if curr_word:
                    words_stack.append(curr_word)
                    curr_word = []
            elif i == len(s) - 1:
                curr_word.append(c)
                words_stack.append(curr_word)
            else:
                curr_word.append(c)

        output = []

        while len(words_stack) > 0:
            output.append("".join(words_stack.pop()))
            if len(words_stack):
                output.append(" ")

        return "".join(output)
    
    # TC: O(n)
    # SC: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        #Trim spaces 
        l_input = self.trim_spaces(s)

        #Reverse entire string
        left, right = 0, len(l_input) - 1
        self.reverse(l_input, left, right)

        #Reverse words
        self.reverse_each_word(l_input)

        return "".join(l_input)

    def reverse_each_word(self, l):
        start = end = 0 
        n = len(l)

        while start < n:
            while end < n and l[end] != " ":
                end += 1

            self.reverse(l, start, end - 1)
            end += 1
            start = end

    def trim_spaces(self, s: str):
        left, right = 0, len(s) - 1

        # remove leading spaces
        while left < right and s[left] == " ":
            left += 1

        #remove trailing spaces
        while right > left and s[right] == " ":
            right -= 1

        # remove extra spaces b/n words
        output = []

        while left <= right:
            if s[left] == " " and left < right and s[left + 1] == " ":
                left += 1
                continue
            else:
                output.append(s[left])
            left += 1

        return output


    def reverse(self, l: list, left: int, right: int):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    
    # TC: O(n)
    # SC: O(n)
        