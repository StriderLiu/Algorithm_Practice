class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, res, [], 0)
        return res

    def dfs(self, cands, tar, res, comb, i):
        if not tar:
            res.append(comb[:])
            return

        for j in range(i, len(cands)):
            if cands[j] > tar:
                return
            if j > i and cands[j] == cands[j - 1]:
                continue

            comb.append(cands[j])
            self.dfs(cands, tar - cands[j], res, comb, j + 1)
            comb.pop()

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
