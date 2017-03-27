class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
    #     # TLE dfs
    #     res = []
    #     self.dfs(n, k, res, [], 1)
    #     return res
    #
    # def dfs(self, n, k, res, comb, i):
    #     if not k:
    #         res.append(comb[:])
    #         return
    #
    #     for j in range(i, n + 1):
    #         comb.append(j)
    #         self.dfs(n, k - 1, res, comb, j + 1)
    #         comb.pop()

        # Use library
        # from itertools import combinations
        # return list(combinations(range(1, n + 1), k))

        # Recursion
        if k == 0:
            return [[]]
        if n < k:
            return []
        return [pre + [i] for i in range(1, n + 1) for pre in self.combine(i - 1, k - 1)]

    #     # Recursion
    #     hash = {}
    #     return self.helper(n, k, hash)
    #
    # def helper(self, n, k, hash):
    #     if k == 0:
    #         return [[]]
    #     if n < k:
    #         return []
    #     if (n, k) in hash:
    #         return hash[(n, k)]
    #
    #     res = []
    #     for i in range(1, n + 1):
    #         for pre in self.combine(i - 1, k - 1):
    #             res.append(pre + [i])
    #     hash[(n, k)] = res
    #     return res

print(Solution().combine(3, 2))