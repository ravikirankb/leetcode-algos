class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = prices[0],0
        for i in range(1,len(prices)):
            if buy > prices[i]:
               buy = prices[i]
            else:
               sell = max(sell,prices[i] - buy)
            
            
        return sell
