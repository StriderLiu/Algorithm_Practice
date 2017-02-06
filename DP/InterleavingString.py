class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        f = [[False for i in range(n + 1)] for j in range(m + 1)]

        for i in range(m + 1):
            f[i][0] = s1[:i] == s3[:i]
        for j in range(n + 1):
            f[0][j] = s2[:j] == s3[:j]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s3[i + j - 1] == s1[i - 1] and s3[i + j - 1] == s2[j - 1]:
                    f[i][j] = f[i - 1][j] or f[i][j - 1]
                elif s3[i + j - 1] == s1[i - 1]:
                    f[i][j] = f[i - 1][j]
                elif s3[i + j - 1] == s2[j - 1]:
                    f[i][j] = f[i][j - 1]

        return f[m][n]

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
s1 = "aabc"
s2 = "abad"
s3 = "aabadabc"
# s1 = "ab"
# s2 = "bc"
# s3 = "bbac"
print(Solution().isInterleave(s1, s2, s3))