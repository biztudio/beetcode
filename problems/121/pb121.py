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
            for j in range(price_index):
                diff = prices[price_index] - prices[j]
                if diff > 0:
                    pass

        return 5