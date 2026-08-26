class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maxProfit = 0
        todaysProfit = 0

        for currPrice in prices:
            if currPrice < minimum:
                minimum = currPrice
                todaysProfit = 0
            todaysProfit = currPrice - minimum
            if todaysProfit > maxProfit:
                maxProfit = todaysProfit
        
        return maxProfit
            