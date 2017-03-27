class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.pair(n, 2, 1, 2)

    def pair(self, n, level, start, end):
        if level == n:
            return '(' + str(start) + ',' + str((n + 1) - start) + ')'

        level *= 2
        left = self.pair(n, level, start, level + 1 - start)
        right = self.pair(n, level, end, level + 1 - end)
        return '(' + left + ',' + right + ')'

print(Solution().findContestMatch(16))