class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = "" 
        for s in strs:
            encoded += str(len(s)) + "#" + s
            
        return encoded
        

    def decode(self, s: str) -> List[str]: 
        decoded = []
        
        left, right = 0, 0
        
        while right < len(s):
            while s[right] != "#":
                right += 1
            len_of_next = int(s[left:right])
            decoded.append(s[right + 1: right + 1 + len_of_next])
            
            right = right + len_of_next + 1
            left = right
            
        return decoded
        
        # encode, decode
        # TC: O(n)
        # SC: O(n + k) K is the extra characters for delimeter and size


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))