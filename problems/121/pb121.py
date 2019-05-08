import pysnooper

class Solution:
    
    @pysnooper.snoop()
    def maxProfit(self, prices) -> int:
        '''
         
        '''
        prices_count = len(prices) 
        if prices_count < 2:
            return 0
        dp = [0 for p in prices]
        
        for price_index in range(1, prices_count):
            if prices[price_index] <= 0 or \
               prices[price_index] <= prices[price_index - 1] or \
               dp[price_index - 1] > prices[price_index]:
                dp[price_index] = dp[price_index - 1]
                continue

            for j in range(price_index):
                diff = prices[price_index] - prices[j]
                dp[price_index] = max(dp[price_index], dp[price_index - 1], diff)

        return dp[-1]