class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            #get last digit by mod to get remender aftr dividing by 2
            # check id the digit is 0 or 1 and increment count 
            res += n % 2
        
            # shift the bit to the right i place to remove last digit checked      
            #n  = n // 2 bit shift is more optinmal on th CPU than integer division
            n = n >> 1
    
        return res
    
    # TC: O(1) ~ 32 chracter bits max
    #SC: O(1)