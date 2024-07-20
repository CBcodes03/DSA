class Solution(object):
    def maxProfit(self, prices):
        mp=0
        cm=prices[0]
        for i in range(len(prices)):
            if cm>prices[i]:
                cm=prices[i]
            if mp<(prices[i]-cm):
                mp = prices[i]-cm
        return mp
