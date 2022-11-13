# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals]);
        end = sorted([i.end for i in intervals])

        res, count = 0, 0

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res




from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(intervals) -> int:

    if not intervals: return 0

    intervals.sort(key=lambda x: x.start)
    rooms = []

    rooms.append(intervals[0])

    for i in range(1, len(intervals)):
        for j in range(len(rooms)):
            if rooms[j].end <= intervals[i].start:
                rooms[j].end = intervals[i].end
                continue
            elif j == len(rooms) - 1:
                rooms.append(intervals[i])

    return len(rooms)
# Time 0(nlogn)
# Space O(N)

intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
print(min_meeting_rooms(intervals))


intervals2 = [Interval(2, 7)]
print(min_meeting_rooms(intervals2))


print(min_meeting_rooms(None))
