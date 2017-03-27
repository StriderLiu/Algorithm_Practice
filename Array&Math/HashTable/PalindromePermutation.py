class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        hash = {}
        for ch in s:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1

        isEven = True
        if n % 2 != 0:
            isEven = False
        cntOdd = 0
        for ch in hash:
            if hash[ch] % 2 == 0:
                continue
            elif not isEven and cntOdd < 1:
                cntOdd += 1
                continue
            else:
                return False
        return True