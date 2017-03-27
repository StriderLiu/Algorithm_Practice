class Solution(object):
    def combinationSum(self, candidates, target):
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
            comb.append(cands[j])
            self.dfs(cands, tar - cands[j], res, comb, j)
            comb.pop()

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))