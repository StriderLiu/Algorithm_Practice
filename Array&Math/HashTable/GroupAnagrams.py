class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        hash = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in hash:
                hash[sortedWord] = [word]
            else:
                hash[sortedWord].append(word)
        res = []
        for key in hash:
            res.append(hash[key])
        return res

print(Solution().groupAnagrams(["", "b"]))
