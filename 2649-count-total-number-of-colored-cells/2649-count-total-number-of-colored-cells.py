class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, Sum  = 0, 1
        while k < n:
            Sum += (4*k)
            k+=1
        return Sum