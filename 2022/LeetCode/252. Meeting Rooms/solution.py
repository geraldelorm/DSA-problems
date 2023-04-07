from ast import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



def can_attend_meetings(intervals) -> bool:
    intervals.sort(key=lambda i: i.start)

    for i in range(len(intervals)):
        if i < len(intervals) - 1 and intervals[i].end > intervals[i + 1].start:
            return False
    return True

#  Time = 
#  Space

# TEST
intervals = [Interval(0, 10), Interval(10, 20), Interval(20, 30)]
print(can_attend_meetings(intervals))

intervals2 = [Interval(5, 8), Interval(9, 15)]
print(can_attend_meetings(intervals2))

intervals3 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
print(can_attend_meetings(intervals3))