#Compare with reverse
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = filter(lambda c: c.isalnum(), s)
        s_lower = map(lambda c: c.lower(), s_filtered)
        s_list = list(s_lower)
        rev_s_list = s_list[::-1]
        
        return  s_list == rev_s_list

    # TC: O(N)
    # SC: O(N)

    
# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNmeric(c):
            return (((ord("A") <= ord(c) and ord("Z") >= ord(c)) 
                    or (ord("a") <= ord(c) and ord("z") >= ord(c))) or 
                   ((ord("0") <= ord(c) and ord("9") >= ord(c))))
            
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not isAlphaNmeric(s[l]):
                l += 1
                
            while l < r and not isAlphaNmeric(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        return True
    
    # TC: O(n)
    # SC: O(1)
    