class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price=prices[0]
        maxm_profit=0

        for i in range(1,len(prices)):
            if prices[i]<buy_price:
                buy_price=prices[i]
            else:
                maxm_profit=max(maxm_profit,(prices[i]-buy_price))
                print(maxm_profit)
        return maxm_profit
            

        