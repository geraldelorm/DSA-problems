import heapq

#Using heap and sorting 
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_count = {}
        for word in words:
            freq_count[word] = freq_count.get(word, 0) + 1

        count_mapping = collections.defaultdict(set)

        for word, count in freq_count.items():
            count_mapping[count].add(word)

        frequency_heap = []

        for count, words in count_mapping.items():
            heapq.heappush(frequency_heap, ( -1 * count, sorted(list(words))))

        res = []

        while len(res) < k:
            words = heapq.heappop(frequency_heap)
            for word in words[1]:
                if len(res) == k:
                    return res
                res.append(word)


        return res


    # TC: O(nlogn (slogs)) n = number of words and s average number of characters in each word
    # SC: O(n)


#heap piority ordering can handle the sorting in python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_count = {}
        for word in words:
            freq_count[word] = freq_count.get(word, 0) + 1


        frequency_heap = []

        for word, count in freq_count.items():
            heapq.heappush(frequency_heap, ( -1 * count, word))

        res = []

        while len(res) < k:
            count, word = heapq.heappop(frequency_heap)
            res.append(word)

        return res

    # TC: O(NLogk) k = different counts
    # SC: O(n)