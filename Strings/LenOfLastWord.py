class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """   
        if s is None or s == '':
            return 0
        
        i = -1
        while i * (-1) <= len(s) and s[i] == ' ':
            i -= 1
        start = i
        
        while i * (-1) <= len(s) and s[i] != ' ':
            i -= 1
        end  = i
        
        return (start - end)
    
print(Solution().lengthOfLastWord('a   '))