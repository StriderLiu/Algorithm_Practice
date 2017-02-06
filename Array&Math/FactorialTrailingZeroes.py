# -*- coding: utf-8 -*-

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        
        cnt = 0
        while n >= 1:
            n = int(n / 5)
            cnt += n
            
        return cnt
        
print(Solution().trailingZeroes(125))