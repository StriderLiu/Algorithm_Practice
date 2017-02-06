class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not len(words) or len(s) < len(words) * len(words[0]):
            return []
        res, N, M, K = [], len(s), len(words), len(words[0])
        allMap, winMap = {}, {}
        
        for word in words:
            if word not in allMap.keys():
                allMap[word] = 1
            else:
                allMap[word] += 1
        rStr, lStr = '', ''
        
        for i in range(K):
            l, count = i, 0
            for r in range(i, N-K+1, K):
                rStr = s[r : (r+K)]  
                if rStr in allMap.keys():
                    if rStr in winMap.keys():
                        winMap[rStr] += 1
                    else:
                        winMap[rStr] = 1
                        
                    if winMap[rStr] <= allMap[rStr]:
                        count += 1
                    
                    while winMap[rStr] > allMap[rStr]:
                        lStr = s[l:l+K]
                        winMap[lStr] -= 1
                        l += K
                        if winMap[lStr] < allMap[lStr]:
                            count -= 1
                
                    if count == M:
                        res.append(l)
                        lStr = s[l:l+K]
                        winMap[lStr] -= 1
                        l += K
                        count -= 1
                
                else:
                    winMap.clear()
                    count = 0
                    l = r + K
                
            winMap.clear()
            
        return res
            
#         if not len(words):
#             return []
#         wordLen, tab, pos, i, res = len(words[0]), {}, 0, 0, []
#         wordCnt, totalWords = 0, len(words)
#         isChanged = False
#         
#         for word in words:
#             if word not in tab.keys():
#                 tab[word] = 1
#             else:
#                 tab[word] += 1
#         
#         while i < len(s):
#             cur = s[i : i + wordLen]
#             if cur in tab.keys() and tab[cur] > 0:
#                 wordCnt += 1
#                 tab[cur] -= 1
#                 if not isChanged:
#                     isChanged = True
#                 
#                 if wordCnt == totalWords:
#                     res.append(pos)
#                     wordCnt = 0 # don't forget this line!
#                     i = pos + 1
#                     pos = i
#                     for word in words: # need to restore the table
#                         tab[word] = 0
#                     for word in words:
#                         tab[word] += 1
#                 else:
#                     i += wordLen
#             else:
#                 if isChanged:
#                     for word in words:
#                         tab[word] = 0
#                     for word in words:
#                         tab[word] += 1
#                     isChanged = False
#                 wordCnt = 0 # And also this line
#                 i = pos + 1
#                 pos = i
#                     
#         return res
    
# s = "wordgoodgoodgoodbestword" # don't forget duplicate words
# words = ["word","good","best","good"]
s = "aaaaaaaa"
words = ["aa","aa","aa"]
print(Solution().findSubstring(s, words))