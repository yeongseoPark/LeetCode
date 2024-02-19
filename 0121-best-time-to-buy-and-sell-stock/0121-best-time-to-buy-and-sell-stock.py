class Solution(object):
    def maxProfit(self, prices):
        ans = 0
        
        buy = 0
        sell = 1
        
        while sell < len(prices):
            cur = prices[sell] - prices[buy]
            
            if cur > 0:
                ans = max(ans, cur)
            
            else:
                buy = sell
            
            sell += 1
                              
        
        return ans 