class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i] :
                    return common_prefix
            
            common_prefix += strs[0][i] 
            
        return common_prefix
    

# Space = O(i)
# Time = O(S) s = sum of length of all stringsin array÷