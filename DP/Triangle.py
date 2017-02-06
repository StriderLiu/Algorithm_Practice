class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        f = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[j] = min(f[j], f[j + 1]) + triangle[i][j] # possible to apply one row instead of a matrix because it can be overwirtten.
        return f[0]

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(Solution().minimumTotal(triangle))