class Solution:
    '''
    problem-url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    '''
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        best=0
        if n==1:
            return 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                best+= prices[i]-prices[i-1]
        return best
