class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            cnt, j, next, m = 0, 0, '', len(s)
            while j < m:
                if m == 1:
                    cnt += 1
                    next += str(cnt) + s[j]
                elif j == 0:
                    cnt += 1
                elif j != 0:
                    if s[j] == s[j-1]:
                        cnt += 1
                    else:
                        next += str(cnt) + s[j-1]
                        cnt = 1
                    if j == m - 1:
                        next += str(cnt) + s[j]
                j += 1
            s = next
                
        return s
    
print(Solution().countAndSay(5))