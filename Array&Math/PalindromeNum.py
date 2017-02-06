# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
#        s = str(x)
#        
#        n = len(s)
#        i, j = 0, n - 1
#        
#        while i <= j:
#            if s[i] != s[j]:
#                return False
#            i += 1
#            j -= 1
#        
#        return True
        # cannot be written as "if not x:", this will include the 0 number
        if x is None:
            return False
        
        # transfer negative number to be positive
        if x < 0:
            return False
        
        # x is only one digit
        if not int(x / 10):
            return True
        
        # count the number of digits in x
        cnt, y = 0, x
        while y > 0:
            cnt += 1
            y = int(y / 10)
        
        # deal with 2-digits case alone
        if cnt == 2:
            if x % 10 == int(x / 10):
                return True
            else:
                return False
        
        # For multiple digits
        i, j = cnt - 1, 0
        while i >= j:
            if int(x / (10 ** i)) % 10 != int(x / (10 ** j)) % 10:
                return False
            i -= 1
            j += 1
        
        return True

# x = None
# x = 0
# x = 1
# x = 12321
# x = 12344321
# x = -2147483648
x = -2147447412
print(Solution().isPalindrome(x))