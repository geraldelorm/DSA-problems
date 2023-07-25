class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prevEnd:
                removals += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
            
        return removals
    
    # TC: O(nlogn)
    # SC: O(1)