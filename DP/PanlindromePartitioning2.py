class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2: return 0

        f = []
        for i in range(n + 1):
            f.append(i - 1)

        isPanlindrome = self.panlindrome(s)
        for i in range(1, n + 1):
            for j in range(i):
                if isPanlindrome[j][i - 1]:
                    f[i] = min(f[i], f[j] + 1)
        return f[n]

    def panlindrome(self, s): # Another DP !!! (区间型)
        n = len(s)
        f = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            f[i][i] = True
        for i in range(n - 1):
            f[i][i + 1] = s[i] == s[i + 1]

        for l in range(2, n): # Out layer iterate the length of the section, inner layer iterate the start point
            for head in range(n - l):
                f[head][head + l] = f[head + 1][head + l - 1] and (s[head] == s[head + l])

        return f

print(Solution().minCut("aab"))