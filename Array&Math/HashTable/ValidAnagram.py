class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash = {}
        for ch in s:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1
        for ch in t:
            if ch not in hash:
                return False
            hash[ch] -= 1
            if hash[ch] < 0:
                return False
        for key in hash:
            if hash[key]:
                return False
        return True