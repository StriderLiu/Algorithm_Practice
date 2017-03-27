class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # f = [[0 for j in range(n)] for i in range(m)]
        # if obstacleGrid[0][0]:
        #     return 0
        # else:
        #     f[0][0] = 1
        #
        # for i in range(m):
        #     for j in range(n):
        #         if j > 0 and not obstacleGrid[i][j]:
        #             f[i][j] += f[i][j - 1]
        #         if i > 0 and not obstacleGrid[i][j]:
        #             f[i][j] += f[i - 1][j]
        #
        # return f[m - 1][n - 1]

        # O(m) space DP
        f = [0 for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            f[i] = 1

        for j in range(1, n):
            for i in range(m):
                if obstacleGrid[i][j]:
                    f[i] = 0
                    continue
                if i > 0:
                    f[i] += f[i - 1]

        return f[m - 1]