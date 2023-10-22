class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        merged_interval = [intervals[0]] 

        for i in range(1, len(intervals)):
            prevEnd = merged_interval[-1][1]
            start, end = intervals[i] 
            if start <= prevEnd:
                merged_interval[-1][1] = max(prevEnd, end)
            else:
                merged_interval.append(intervals[i])

        return merged_interval

        # TC: O(nlogN)
        # SC: O(n)