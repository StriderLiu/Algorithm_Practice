class Solution(object):
    def missingWords(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: list
        """
        if not s:
            return []
        if not t:
            return s.split(' ')
        
        s_arr = s.split(' ')
        t_arr = t.split(' ')
        res, i, j = [], 0, 0
        
        while j < len(t_arr):
            if s_arr[i] == t_arr[j]:
                j += 1
            else:
                res.append(s_arr[i])
            i += 1
        
        if i < len(s_arr):
            res += s_arr[i:]
        
        return res
        
#         res = []
#         i, j, pos = 0, 0, 0
#         ls, lt = len(s), len(t)
#         
#         # The key is to get the hang of the different word match cases (4).
#         while i < ls and j < lt:
#             p, q = i, j
#             # Need to figure out what's the sign of completing a word matching
#             while q < lt and s[p] == t[q] and s[p] != ' ':
#                 p += 1
#                 q += 1
#             
#             isMatch = False
#             # In what condition does two words match?
#             if q == lt or t[q] == ' ':
#                 isMatch = True
#                                           
#             if not isMatch: # not match, jump to the next word or end
#                 while i < ls and s[i] != ' ':
#                     i += 1
#                 if i < ls:
#                     res.append(s[pos: i])
#                     i += 1
#                     pos = i
#             else:
#                 if q == lt and p < ls:
#                     res += s[p+1:].split(' ')
#                     return res  
#                 i, j, pos = p+1, q+1, p+1
#                 
#         return res

print(Solution().missingWords('I am using hackerrank to improve programming', 'am hackerrank to improve'))


