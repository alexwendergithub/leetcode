class Solution {
    public int maxProfit(int[] prices) {
        int buyingPrice = prices[0];
        int sellingPrice = prices[0];
        int stonks = 0;
        for (int i=0;i<prices.length;i++){
            if (prices[i] < buyingPrice){
                buyingPrice = prices[i];
                sellingPrice = prices[i];
            }
            if (prices[i] > sellingPrice){
                if (prices[i]-buyingPrice>stonks){
                    sellingPrice = prices[i];
                    stonks = prices[i]-buyingPrice;
                }
            }
        }
        return stonks;
    }
}