class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        T = []
        for i in range(numRows):
        	li = []

        	for j in range(i + 1):
        		if j == 0 or j == i:
        			li.append(1)
        		else:
        			li.append(T[i - 1][j - 1] + T[i - 1][j])

        	T.append(li)

        return T

if __name__ == '__main__':
	numRows = 10
	print(Solution().generate(numRows))