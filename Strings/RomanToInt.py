class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val, i = 0, 0
        
        while i < len(s):
            if i+1 < len(s) and dict[s[i+1]] > dict[s[i]]:
                val += dict[s[i+1]] - dict[s[i]]
                i += 2
            else:
                val += dict[s[i]]
                i += 1
                
        return val

print(Solution().romanToInt("DCXXI"))