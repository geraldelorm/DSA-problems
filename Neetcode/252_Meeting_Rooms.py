class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda i: i[0])
        
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                return False
            prev_end = end
                  
        return True
    
    # TC: O(NlogN)
    # SC: O(1)