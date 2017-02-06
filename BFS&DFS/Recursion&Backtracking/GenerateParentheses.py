class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        res = []
        self.dfs(res, n, n, 0, '')
        return res
    
    def dfs(self, res, n, m, done, s):
        if len(s) == 2 * n:
            res.append(s)
            return
        
        for i in range(int(not bool(n - m - done)), m + 1):
            self.dfs(res, n, m - i, done + 1, s + '(' * i + ')')
        
print(Solution().generateParenthesis(4))