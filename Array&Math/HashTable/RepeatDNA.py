class Solution(object):
    def findRepeatedDnaSequences(self, s):
        hash, res, n = set(), set(), len(s)
        if n <= 10:
            return res
        for i in range(n - 9):
            sub = s[i : i + 10]
            if sub not in hash:
                hash.add(sub)
            else:
                res.add(sub)
        return res

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))