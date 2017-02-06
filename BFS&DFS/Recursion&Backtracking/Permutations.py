class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(ans, [], nums)
        return ans

    def dfs(self, ans, cur, rest):
        if not rest:
            ans.append(cur[:])
            return
        
        for i in range(len(rest)):
            if len(rest) == 1:
                self.dfs(ans, cur + [rest[i]], [])
            else:
                self.dfs(ans, cur + [rest[i]], rest[:i] + rest[i+1:])

print(Solution().permute([1, 2, 3, 4, 5, 6, 7, 8]))
