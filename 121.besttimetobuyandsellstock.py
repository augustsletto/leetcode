class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float("inf")        
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
                
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
    
solution = Solution()


print(solution.maxProfit([1, 2, 3, 4, 5]))