# -*- coding: utf-8 -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # Filter whitespaces
        str = str.lstrip()
        
        # Return 0 for empty input
        if not str:
            return 0
        
        # a flag indicating res is negative or not
        # start and end index indicating the valid number
        isNeg, start, end, res = False, -1, 0, 0
        
        # Check the first element
        # The only valid value for str[0] is '+', '-' or number in 0 to 9
        if str[0] == '-':
            isNeg = True
        elif ord(str[0]) <= ord('9') and ord(str[0]) > ord('0'):
            start = 0
            if len(str) == 1:
                end = 1
        elif str[0] != '+' and str[0] != '0':
            return res
            
        for i, c in enumerate(str[1:]):
            # If we encounter value other than number, the loop stops cuz we have found the end index
            if ord(c) > ord('9') or ord(c) < ord('0'):
                end = i + 1
                break
            # Filter prefix 0s
            if c == '0' and start == -1:
                continue
            # If the str[0] is not number in 1 to 9 and start has never been set
            if (ord(str[0]) > ord('9') or ord(str[0]) <= ord('0')) and start == -1:
                start = i + 1
        else:
            end = len(str)
                
        if start == -1:
            return res
            
        n = end - start - 1
        for i in range(start, end):
            res += (ord(str[i]) - ord('0')) * (10 ** n)
            n -= 1
        
        # Dealing with 'out of range' case
        if isNeg:
            res *= -1
            res = max(res, -2147483648)
            
        res = min(res, 2147483647)
            
        return res

# str = '   -0123ab5E'
# str = '1'
# str = '-1'
# str = '    +0a32'  
str = "2147483648"  
print(Solution().myAtoi(str))