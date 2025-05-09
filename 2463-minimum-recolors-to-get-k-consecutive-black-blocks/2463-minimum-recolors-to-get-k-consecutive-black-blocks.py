class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        
        n = len(blocks)
        minColor = k
        curr = 0
        for i in range(k):
            if blocks[i] == 'W':
                curr += 1
        minColor = curr
        for i in range(k, n):
            if blocks[i - k] == 'W':
                curr -= 1
            if blocks[i] == 'W':
                curr += 1
            minColor = min(minColor, curr)
        return minColor