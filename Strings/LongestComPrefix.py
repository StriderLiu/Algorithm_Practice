import sys

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or strs == []:
            return ''
        
        # find the minimum length
        minLen = sys.maxsize
        minStr = ''
        for s in strs:
            if minLen > len(s):
                minLen = len(s)
                minStr = s
                
        flag = False
        lcp = ''
        for i in range(minLen):
            for s in strs:
                if s[i] != minStr[i]:
                    flag = True
                    break
            if flag is True:
                break
            else:
                lcp += minStr[i]
        
        return lcp
    
print(Solution().longestCommonPrefix(['a', 'asd', 'asdfg', 'asdffasdfasfgh', 'asdefew']))