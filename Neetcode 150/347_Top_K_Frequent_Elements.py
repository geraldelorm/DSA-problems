class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the appearance of unique elements ~ map
        appearance = {} #3: 1, 0: 2, 1: 1
        
        for n in nums:
            appearance[n] = appearance.get(n, 0) + 1
        #for k time find the top appearing elemets and remove it from the storage bucket
        
        res = [] 
        
        for i in range(k):
            top, topVal = 0, 0
            for k in appearance:
                if appearance[k] > topVal:
                    top = k
                    topVal = appearance[k]
            res.append(top)
            del appearance[top]
            
        return res
    
    # TC: O(kN)
    # SC: O(k + N)
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appearance = {}
        count = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            appearance[n] = appearance.get(n, 0) + 1
            
        for key in appearance:
            count[appearance[key]].append(key)      
        
        res = []
        for i in range(len(count) - 1, 0, -1):      
            for v in count[i]:
                res.append(v)
                if len(res) == k:
                    return res
    
    # TC: O(k + N)
    # SC: O(k + N)