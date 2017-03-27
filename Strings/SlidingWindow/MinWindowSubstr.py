class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lenS, lenT = len(s), len(t)
        if not lenS or not lenT or lenS < lenT:
            return ''

        hash = [0 for i in range(256)]
        for ch in t:
            hash[ord(ch)] += 1

        i, j = 0, 0
        minRange, numEmerge = (0, lenS), 0
        for i in range(lenS):
            if hash[ord(s[i])] > 0:
                numEmerge += 1
            hash[ord(s[i])] -= 1

            while numEmerge >= lenT:
                if minRange[1] - minRange[0] > i - j:
                    minRange = (j, i)
                hash[ord(s[j])] += 1
                if hash[ord(s[j])] > 0:
                    numEmerge -= 1
                j += 1

        if minRange == (0, lenS):
            return ''
        return s[minRange[0]: minRange[1] + 1]