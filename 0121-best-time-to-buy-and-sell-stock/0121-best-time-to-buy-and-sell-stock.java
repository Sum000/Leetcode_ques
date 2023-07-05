class Solution {
    public int maxProfit(int[] prices) {
        int minStock = prices[0];
        int maxProfit = 0;
        
        for (int i = 0; i < prices.length; i++){
           
              minStock = Math.min(minStock, prices[i]);
              int profit = prices[i] - minStock;
              maxProfit = Math.max(profit, maxProfit);
        }
        return maxProfit;
    }
}