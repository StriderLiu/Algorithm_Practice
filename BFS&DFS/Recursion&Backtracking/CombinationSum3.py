class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, tar, i, comb, res):
        if tar < 0 or (not k and tar > 0):
            return
        if not tar and not k:
            res.append(comb[:])
            return

        for j in range(i, 10):
            comb.append(j)
            self.dfs(k - 1, tar - j, j + 1, comb, res)
            comb.pop()

k, n = 3, 7
print(Solution().combinationSum3(k, n))