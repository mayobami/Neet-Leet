class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        high=0
        for r in range(r,len(prices)):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                high=max(high,profit)
            else:
                l=r
        return high
