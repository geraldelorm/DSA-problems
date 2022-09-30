class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

# Time / space = O(n)
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        decoded, i = [], 0
        "10#kofiyhdgte3#Ama5#Amina"

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1

            lenght = int(str[i:j])
            decoded.append(str[j + 1: j + 1 + lenght])
            r = j + 1 + lenght

        return decoded

# Time / space = O(n)
