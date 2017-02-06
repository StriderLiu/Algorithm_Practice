# -*- coding: utf-8 -*-

class Solution(object):
    def __init__(self):
        self.low = 0
        self.maxLen = 0
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
            
        for i in range(len(s) - 1):
            self.probePalindrome(s, i, i)
            self.probePalindrome(s, i, i + 1)
            
        return s[self.low : self.low + self.maxLen]
    
    def probePalindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
            
        if k - j - 1 > self.maxLen:
            self.maxLen = k - j - 1
            self.low = j + 1
            
print(Solution().longestPalindrome('asdfneveroddorevenhrt'))