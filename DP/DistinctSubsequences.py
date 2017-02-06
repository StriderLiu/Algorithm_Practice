class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if m < n: return 0
        f = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            f[i][0] = 1
            for j in range(1, n + 1):
                if i < j:
                    f[i][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]

        return f[m][n]

s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))