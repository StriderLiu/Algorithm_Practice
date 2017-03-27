class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, p1, p2 = len(words), -1, -1
        minDist = n
        for i in range(n):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                if word1 == word2:
                    p1 = p2
                p2 = i

            if p1 != -1 and p2 != -1:
                minDist = min(minDist, abs(p2 - p1))
        return minDist