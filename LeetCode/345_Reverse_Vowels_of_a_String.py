class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        output = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


        for c in s:
            if c in vowels:
                stack.append(c)
        
        for c in s:
            if c in vowels:
                output.append(stack.pop())
            else:
                output.append(c)

        return "".join(output)

        # TC: O(n)
        # SC: O(n)
        




class Solution:
    def reverseVowels(self, s: str) -> str: #s = "hello"
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        start, end = 0, len(s) - 1 #1, 3
        s_list = list(s)

        def swap(i, j):
            s_list[i], s_list[j] = s_list[j], s_list[i]

        while start < end:
            while start < end and not s_list[start] in vowels:
                start += 1

            while end > start and not s_list[end] in vowels:
                end -= 1

            if s[start] in vowels and s_list[end] in vowels:
                swap(start, end)
        
            start += 1
            end -= 1
            

        return "".join(s_list)
    
        # TC: O(n)
        # SC: O(n)      