class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRes = 0
        l= 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxRes = max(profit, maxRes)
            if prices[r] >= prices[l]:
                r +=1
            else:
                l=r

        return maxRes

        
        