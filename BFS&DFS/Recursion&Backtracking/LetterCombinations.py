# -*- coding: utf-8 -*-

class Solution(object):
    def __init__(self):
        self.d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' ']
        }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
            return res
        self.dfs(res, digits, 0, '')
        return res
        
    def dfs(self, res, digits, i, cur):
        if i == len(digits):
            res.append(cur)
            return
            
        for j in range(len(self.d[digits[i]])):
            self.dfs(res, digits, i + 1, cur + self.d[digits[i]][j])
            
digits = '4567890'
print(Solution().letterCombinations(digits))