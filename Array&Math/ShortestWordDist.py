class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(words)
        p1, p2, minDist = -1, -1, n
        for i in range(n):
            if words[i] == word1:
                p1 = i

            if words[i] == word2:
                p2 = i

            if p1 != -1 and p2 != -1:
                minDist = min(minDist, abs(p1 - p2))
        return minDist