import sys


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        # For comprehension
        f = [[sys.maxsize for j in range(n + 1)] for i in range(m + 1)] # Note how to initialize a 2d array!

        for i in range(m + 1):
            f[i][0] = i
        for j in range(n + 1):
            f[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)

        return f[m][n]

word1 = "b"
word2 = ""
print(Solution().minDistance(word1, word2))