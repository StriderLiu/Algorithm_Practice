class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Traditional Solution (DP):
        pat = list(p)
        str = list(s)
        writeIndex = 0
        isFirst = True
        for i in range(len(p)):
            if pat[i] is '*':
                if isFirst:
                    pat[writeIndex] = pat[i]
                    writeIndex += 1
                    isFirst = False
            else:
                pat[writeIndex] = pat[i]
                writeIndex += 1
                isFirst = True
                 
        T = [[False for x in range(writeIndex + 1)] for x in range(len(str) + 1)]
         
        if writeIndex > 0 and pat[0] is '*':
            T[0][1] = True
        T[0][0] = True
        
        for i in range(1, len(T)):
            for j in range(1, len(T[0])):
                if pat[j - 1] is '?' or pat[j - 1] is str[i - 1]:
                    T[i][j] = T[i - 1][j - 1]
                elif pat[j - 1] is '*':
                    T[i][j] = T[i - 1][j] or T[i][j - 1]
                 
        return T[len(str)][writeIndex]

# Special Solution:
#     Loop
#         1. keep two pointers in S and P here i and j
# 
#         2. if S[i] == P[j] or P[j] == '?' we keep moving
# 
#         3. if '*' exist in P then we mark the position in P as star and mark position in s as s_star
#         4. Loop over s until S[i] == P[star + 1] otherwise False
#
#     note that S = 'a' P = 'a*******' is still True So we need to loop over P to check this case
#     if we can compare p to the end that means True
    
#         i = 0
#         j = 0
#         star = -1
#         s_star = 0
#         s_len = len(s)
#         p_len = len(p)
#         while i < s_len:
#             if i < s_len and j < p_len and p[j] in (s[i], '?'):
#                 i += 1
#                 j += 1
#             elif j < p_len and p[j] == '*':
#                 star = j
#                 s_star = i
#                 j += 1
#             elif star != -1:
#                 j = star + 1
#                 s_star += 1
#                 i = s_star
#             else:
#                 return False
#         while j < p_len and p[j] == '*':
#             j += 1
#         return j == p_len
    
# if __name__ is '__main__':
print(Solution().isMatch('xaylmz', 'x?y*z'))