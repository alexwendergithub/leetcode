class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = prices[0]
        sellingPrice = prices[0]
        stonks = 0
        for i in range(len(prices)):
            if prices[i] < buyingPrice:
                buyingPrice = prices[i]
                sellingPrice = prices[i]
            if prices[i] > sellingPrice:
                if prices[i]-buyingPrice>stonks:
                    sellingPrice = prices[i]
                    stonks = prices[i]-buyingPrice
        return  stonks
