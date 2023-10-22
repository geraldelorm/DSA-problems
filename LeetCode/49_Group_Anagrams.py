class Solution:
    #     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #         if strs == None or len(strs) < 1: return []

    #         hashmap = {}

    #         for i in range(len(strs)):
    #             sortedS = str(sorted(strs[i]))
    #             if sortedS in hashmap:
    #                 hashmap[sortedS].append(strs[i])
    #             else:
    #                 hashmap[sortedS] = [strs[i]]

    #         return [i for i in hashmap.values()]

    # #     Time = O(m * nlogn)
    # #     Space = O(m)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            countKey = self.getCount(strs[i])
            if countKey in hashmap:
                hashmap[countKey].append(strs[i])
            else:
                hashmap[countKey] = [strs[i]]

        return [i for i in hashmap.values()]

    def getCount(self, s):
        count = [0] * 26  # get of characters a .... z

        for c in s:
            count[ord(c) - ord("a")] += 1

        return tuple(count)  # or just string

#     Time = O(m * n) m == array n == len of string
#     Space = O(m) + 26 index array + call stack for the funtion getCount call
