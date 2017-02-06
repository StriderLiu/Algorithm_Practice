import math

# This can be solved in O(1) time
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
    
n = 99999999
print(Solution().bulbSwitch(n))