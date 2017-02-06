# Divide two integers without using multiplication, division and mod operator.
# 
# If it is overflow, return MAX_INT.

import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isNeg = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            isNeg = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        current, res = 1, 0
        
        while divisor <= dividend:
            divisor <<= 1
            current <<= 1
             
        divisor >>= 1
        current >>= 1
        while current != 0:
            if dividend >= divisor:
                dividend -= divisor
                res |= current
            divisor >>= 1
            current >>= 1
        
        
        if isNeg:
            return -res
        else:
            res = min(res, 2147483647)   
            return res
  
dividend, divisor = -1, 1 
print(Solution().divide(dividend, divisor))