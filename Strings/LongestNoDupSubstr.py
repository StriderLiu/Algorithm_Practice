# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        if len(s) == 1:
            return 1
            
        d, j, maxLen = {}, 0, 1
        
        # A sliding window is an abstract concept commonly used in array/string problems.
        for i, c in enumerate(s):
            if c in d.keys():
                j = max(j, d[c] + 1)
            d[c] = i
            maxLen = max(maxLen, i - j + 1)
            
        return maxLen
        
print(Solution().lengthOfLongestSubstring('kwwkew'))