class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxprof = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                prof =  prices[r] - prices[l]
                maxprof = max(maxprof, prof)
            else:
                l= r
            r+=1
        return maxprof