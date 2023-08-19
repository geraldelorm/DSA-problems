class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        appearances = [[]] * (len(s) + 1)

        for k in count:
            appearances[count[k]] = appearances[count[k]] + [k]
            
        output = []
        for i in range(len(appearances) - 1, -1, -1):
            for c in appearances[i]:
                output.append(c * i)

        return "".join(output)

        # TC: O(n) ~ 2n
        # SC: O(n) ~ 2n


# Done neatly with Counter properties by sorting by most common
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
            
        output = []
        for letter, freq in counts.most_common():
            output.append(letter * freq)

        return "".join(output)


        # TC: O(nlogn) ~srting by freq
        # SC: O(n)
