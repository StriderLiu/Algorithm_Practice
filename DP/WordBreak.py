class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        f = [True] + [False] * n # (n+1) array
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        for i in range(1, n + 1): # out layer range from 1 to n+1, inner layer range from 0 to i
            # j is the length start from i to its left
            for j in range(1, min(maxLen, i) + 1): # Note how to minimumize the number of iteration
                if not f[i - j]:
                    continue
                if s[i - j: i] in wordDict:
                    f[i] = True
                    break

        return f[n] # return Nth element

s = "leetcode"
dict = ["leet", 'code']
print(Solution().wordBreak(s, dict))