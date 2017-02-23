# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from operator import attrgetter


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        size = len(intervals)
        if size < 2:
            return intervals

        # sort by interval start
        intervals = sorted(intervals, key=attrgetter('start'))

        # iterate thru intervals to see if adjacent intervals can merge:
        cur, res = intervals[0], []
        for interval in intervals[1:]:
            if interval.start <= cur.end:  # can merge
                cur = Interval(cur.start, max(cur.end, interval.end))
            else:
                res.append(cur)
                cur = interval
        res.append(cur)

        return res
