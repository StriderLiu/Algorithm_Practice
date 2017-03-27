class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hash = {0: 1}
        return self.dfs(nums, target, hash)

    def dfs(self, nums, tar, hash):
        # DP (hash) + dfs
        if tar in hash:
            return hash[tar]

        cnt = 0
        for num in nums:
            if num <= tar:
                cnt += self.dfs(nums, tar - num, hash)
        hash[tar] = cnt
        return cnt

nums = [4, 2, 1]
target = 32
print(Solution().combinationSum4(nums, target))