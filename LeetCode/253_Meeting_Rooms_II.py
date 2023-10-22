class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        
        i = j = 0
        count = max_count = 0
        
        while i < len(start_times) and j < len(end_times):
            if start_times[i] < end_times[j]:
                count += 1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                j += 1
                
        return max_count
            
        
    # TC: O(nlogN)
    # SC: O(N)