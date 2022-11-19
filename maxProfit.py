class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
    
        #1,2,3,4,5 
        #i = 0
        #min_price = 1
        #i = 1, elif block => max_profit = 1-2 