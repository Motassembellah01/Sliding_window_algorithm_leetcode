from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximProf = 0
        l = 0
        r = 1
        while r < len(prices):
            profit = prices[r] - prices[l] 
            maximProf = max(maximProf, profit)
            if prices[l] > prices[r]:
                l = r
            r += 1
        return maximProf