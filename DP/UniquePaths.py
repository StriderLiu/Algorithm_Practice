class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m and not n:
            return 0

        # # O(mn) Space
        # f = [[0 for j in range(n)] for j in range(m)]
        #
        # for i in range(m):
        #     for j in range(n):
        #         if not i and not j:
        #             f[i][j] = 1
        #         if i > 0:
        #             f[i][j] += f[i - 1][j]
        #         if j > 0:
        #             f[i][j] += f[i][j - 1]
        #
        # return f[m - 1][n - 1]

        # O(min(m, n)) Space
        if m > n:
            return self.uniquePaths(n, m)

        curCol = [1 for i in range(m)]
        for j in range(1, n):
            for i in range(1, m):
                curCol[i] += curCol[i - 1]
        return curCol[m - 1]