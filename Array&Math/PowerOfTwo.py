class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if not n % 2:
                n /= 2
                continue
            
            return False
        
        return n == 1
    
print(Solution().isPowerOfTwo(1))