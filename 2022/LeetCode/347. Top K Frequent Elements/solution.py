from heapq import heappop, heappush


class Solution:
    #     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #         frequents, hashmap = [], {}

    #         for n in nums:
    #             hashmap[n] = hashmap.get(n, 0) + 1

    #         for i in range(k):
    #             maxVal = [0, 0]
    #             for k in hashmap:
    #                 if hashmap[k] > maxVal[1]:
    #                     maxVal = [k, hashmap[k]]

    #             frequents.append(maxVal[0])
    #             del hashmap[maxVal[0]]

    #         return frequents

    #     Time = O(n + k.n)
    #     Space = O(n)

    # Using a heap
    #  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #         if not nums:
    #             return []

    #         if len(nums) == 1:
    #             return nums

    #         frequents, hashmap = [], {}

    #         for n in nums: #n
    #             hashmap[n] = hashmap.get(n, 0) - 1 #to get a maxheap we negate values

    #         heap = []

    #         for key in hashmap: #n
    #             heappush(heap, (hashmap[key], key))

    #         count = 0
    #         while count < k: #klogn
    #             print(count)
    #             freq, item = heappop(heap)
    #             frequents.append(item)
    #             count += 1

    #         return frequents

    #    Time =
    #    Space = O(n)

    # We can improve this using a variation of bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for key in hashmap:
            freq[hashmap[key]].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

#     Time = O(n)
#     Space = O(n)
