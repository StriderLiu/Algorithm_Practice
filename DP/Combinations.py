class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # # TLE DP
        # dp = [[[[]] for j in range(k + 1)] for i in range(n + 1)]
        # for i in range(1, n + 1):
        #     dp[i][1] = [[j] for j in range(1, i + 1)]
        #     if i <= k:
        #         dp[i][i] = [[j for j in range(1, i + 1)]]
        #
        # for col in range(2, k + 1):
        #     for row in range(col + 1, n + 1):
        #         dp[row][col] = dp[row - 1][col] + [comb + [row] for comb in dp[row - 1][col - 1]]
        #
        # return dp[n][k]

print(Solution().combine(5, 3))