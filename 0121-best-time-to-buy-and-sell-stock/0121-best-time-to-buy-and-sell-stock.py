class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left=0 #for buying
        right=1 # for selling
        profit=0
        n=len(prices)
        while right<n:
            curr_pro=prices[right]-prices[left]
            if prices[left]<prices[right]:
                profit=max(curr_pro,profit)
            else:
                left=right
            right+=1
        return profit
        