class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # O(logN)
        val, i = num - 1, 2
        while i * i <= num:
            if not num % i:
                val -= i + int(num / i)
            i += 1
        if num == (i - 1) * (i - 1):
            val += i - 1
        return val == 0
print(Solution().checkPerfectNumber(28))