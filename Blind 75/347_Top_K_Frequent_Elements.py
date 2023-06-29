#Using a frequency Map
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        frequencyMap = {}
        
        for n in nums:
            frequencyMap[n] = frequencyMap.get(n, 0) + 1

        ans = []
        for i in range(k):
            maxk, maxv = 0, 0
            for k in frequencyMap:
                if frequencyMap[k] > maxv:
                    maxv = frequencyMap[k]
                    maxk = k
            ans.append(maxk)
            del frequencyMap[maxk]
            
        return ans
    
# Time = O(NK) or O(N) if len(nums) N is > k
# Space = O(N) or N + K


#Using a frequency Map and a Max heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
    
# Time = O(NlogK) 
# Space = O(N + k)
        
    
#Using a frequency Map and bucket sort approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        frequencyMap = {}
        bucket = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            frequencyMap[n] = frequencyMap.get(n, 0) + 1
            
        for i, v in frequencyMap.items():
            bucket[v].append(i)

        ans = []
        for i in range(len(bucket) -1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans        
    
# Time = O(N)
# Space = O(N)