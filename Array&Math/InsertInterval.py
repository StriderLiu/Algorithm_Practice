# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        if not n:
            return [newInterval]

        res, i, hasInserted = [], 0, False
        while i < n:
            if newInterval.start > intervals[i].end:
                res.append(intervals[i])
            elif newInterval.end < intervals[i].start:
                res.append(newInterval)
                hasInserted = True
                break
            else:
                newInterval.start, newInterval.end = min(intervals[i].start, newInterval.start), max(intervals[i].end,
                                                                                                     newInterval.end)
            i += 1
        if hasInserted:
            res += intervals[i:]
        else:
            res.append(newInterval)
        return res
