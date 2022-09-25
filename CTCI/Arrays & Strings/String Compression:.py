# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress(s):
    if len(s) < 3:
        return s
    newString = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 > len(s) - 1 or s[i] != s[i + 1]:
            newString.append("" + s[i] + str(count))
            count = 0

    if len(newString) < len(s):
        return "".join(newString)
    return s
# Time = O(n)
# Space = O(n)


assert(compress("aabcccccaaa") == "a2b1c5a3")
assert(compress("aa") == "aa")
assert(compress("abc") == "abc")

# We can improve this by checking if comprssed lenght will be short b4 we use up the array space - this implies having an initial loop to check for that
