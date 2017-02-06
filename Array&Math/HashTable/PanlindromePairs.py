class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        if n < 2:
            return []
        res, hash = [], {}
        for i, word in enumerate(words):
            hash[word] = i
        # O(n * k^2)
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                leftRsv, rightRsv = left[::-1], right[::-1]
                if self.isPanlindrome(left) and rightRsv in hash and hash[rightRsv] != i:
                    res.append([hash[rightRsv], i])
                if self.isPanlindrome(right) and leftRsv in hash and hash[leftRsv] != i and len(right):
                    res.append([i, hash[leftRsv]])
        return res

    def isPanlindrome(self, string):
        i, j = 0, len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True