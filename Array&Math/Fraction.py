class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res, hash = '', {}
        isNeg = (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)
        # 6 / 3 = '2'
        res += str(numerator // denominator)
        if numerator % denominator != 0:
            res += '.'
        numerator %= denominator

        ind = len(res) - 1
        # 1 / 2 = '0.5', # 1 / 6 = '0.1(6)', 15 / 7 = '2.(142857)'
        while numerator != 0:
            numerator *= 10
            if numerator in hash:
                res = res[:hash[numerator]] + '(' + res[hash[numerator]:] + ')'
                break
            res += str(numerator // denominator)
            ind += 1
            hash[numerator] = ind
            numerator %= denominator

        if isNeg:
            return '-' + res
        return res

print(Solution().fractionToDecimal(1, 21476834))