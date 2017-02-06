# -*- coding: utf-8 -*-

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Add sentinal to both        
        s , p = '~' + s, '~' + p
        lenS, lenP = len(s), len(p)
        T = []
        
        # Use DP
        for i in range(lenS):
            li = []
            for j in range(lenP):
                li.append(False)
            T.append(li)
        T[0][0] = True
        
        for i in range(lenS):
            for j in range(1, lenP):
                # If we encounter a char comes with '*'
                if j < lenP - 1 and p[j + 1] == '*':
                    # Solve the pattern '.*'
                    if p[j] == '.' and j == 1:
                        T[i][j] = T[0][0]
                    else:
                        k = i
                        while k >= 0:
                            T[i][j] = T[k][j - 1]
                            if (p[j] != '.' and p[j] != s[k]) or T[i][j]:
                                break
                            k -= 1
                # If we encounter a '*'
                elif p[j] == '*':
                    T[i][j] = T[i][j - 1]
                # If we encounter '.' in p or same char with s[i], 
                # at the mean while no '*' after this '.'
                elif (p[j] == '.' or p[j] == s[i]) and i > 0:
                    T[i][j] = T[i - 1][j - 1]
                    
        # The last element of the DP diagram is the result we want
        return T[lenS - 1][lenP - 1]

#s = 'aab'
#p = 'c*a*b'
        
#s = 'aaa'
#p = 'ab*a*c*a'
        
s = 'ab'
p = '.*'
print(Solution().isMatch(s, p))