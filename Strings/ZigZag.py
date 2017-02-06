class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        res, m = '', len(s)
        
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < m:
                    res += s[j]
                    j += 2 * numRows - 2
            
            else:
                j = i
                while j < m:
                    res += s[j]
                    if 2 * numRows - 2 + j - 2 * i < m:
                        res += s[2 * numRows - 2 + j - 2 * i]
                    j += 2 * numRows - 2
                    
        return res
                    
s = 'XUWEIJIA'
numRows = 3
print(Solution().convert(s, numRows))