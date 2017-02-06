class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        extra = 0
        if digits[-1] + 1 > 9:
            digits[-1] = 0
            extra = 1
        else:
            digits[-1] += 1
            return digits

        for i in range(n - 2, -1, -1):
            if digits[i] + extra < 10:
                digits[i] += extra
                return digits
            else:
                digits[i] = 0

        return [1] + digits