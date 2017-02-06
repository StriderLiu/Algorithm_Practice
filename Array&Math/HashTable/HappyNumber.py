# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # hash, res = set(), n
        # while True:
        #     res = self.digSqrSum(res)
        #     if res == 1:
        #         return True
        #     if res in hash:
        #         return False
        #     hash.add(res)

        # O(1) Space
        # Fast-slow pointer
        slow, fast = n, n
        while True:
            slow = self.digSqrSum(slow)
            fast = self.digSqrSum(fast)
            fast = self.digSqrSum(fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False

    def digSqrSum(self, n):
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n = int(n / 10)
        return sum

print(Solution().isHappy(7))