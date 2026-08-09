class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRes = 0
        left = 0
        right = len(prices)-1

        while left < right:
            res = prices[right]-prices[left]
            maxRes = max(res, maxRes)
            if left + 1 < len(prices)-1 and right -1 > 0 and ((prices[left] - prices[left+1]) > prices[right-1] - prices[right]):
                left +=1
            else:
                right -=1

        return maxRes

        
        