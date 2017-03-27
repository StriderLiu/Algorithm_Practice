class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, res, [], 2)
        return res

    def dfs(self, n, res, path, start):
        if n < 4:
            return

        for divisor in range(start, n // 2 + 1):
            if n % divisor:
                continue
            quotient = n // divisor
            if quotient < divisor:
                continue

            path.append(divisor)
            path.append(quotient)
            res.append(path[:])
            path.pop()
            self.dfs(quotient, res, path, divisor)
            path.pop()

print(Solution().getFactors(32))