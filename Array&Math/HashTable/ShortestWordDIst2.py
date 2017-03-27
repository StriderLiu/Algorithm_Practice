class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # # O(n^2) when number of shortest() calling is greater than n, this way is better
        # self.dict = {}
        # n = len(words)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if (words[i], words[j]) in self.dict:
        #             self.dict[(words[i], words[j])] = min(self.dict[(words[i], words[j])], j - i)
        #         elif (words[j], words[i]) in self.dict:
        #             self.dict[(words[j], words[i])] = min(self.dict[(words[j], words[i])], j - i)
        #         else:
        #             self.dict[(words[i], words[j])] = j - i

        self.dict = {word: [] for word in words}
        for i in range(len(words)):
            self.dict[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # # O(1)
        # if (word1, word2) in self.dict:
        #     return self.dict[(word1, word2)]
        # if (word2, word1) in self.dict:
        #     return self.dict[(word2, word1)]

        # O(freq_w1 + freq_w2)
        minDist = float('inf')
        posList1, posList2 = self.dict[word1], self.dict[word2]
        i, j = 0, 0
        while i < len(posList1) and j < len(posList2):
            minDist = min(minDist, abs(posList1[i] - posList2[j]))
            if posList1[i] < posList2[j]:
                i += 1
            else:
                j += 1
        return minDist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)