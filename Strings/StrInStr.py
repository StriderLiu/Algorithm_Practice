# Returns the index of the FIRST occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(needle), len(haystack)
        # Null Input case
        if not m and not n:
            return 0
        
        i = 0
        while i < n:
            # Tail of haystack does not match
            if i + m > n:
                break
            pos = i
            j, k = 0, m - 1
            while j <= k and haystack[i] == needle[j] and haystack[i + k - j] == needle[k]:
                i += 1
                j += 1
                k -= 1
            if j > k:
                return i - j
            i = pos + 1
        return -1
    
# haystack = "sssssssssb"
# needle = "ssssssssb"

haystack = "mississippi"
needle = "sipp"
print(Solution().strStr(haystack, needle))