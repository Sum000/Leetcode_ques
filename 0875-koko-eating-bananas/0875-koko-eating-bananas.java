class Solution {
    static int max(int[] piles) {
        int max = Integer.MIN_VALUE;
        int n = piles.length;
        
        for (int i = 0; i < n; i++)
            max = Math.max(max, piles[i]);
        
        return max;
    }
    
    public int minEatingSpeed(int[] piles, int h) {
        int l = 0;
        int r = max(piles);
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int totalH = time(piles, mid);
            
            if (totalH <= h)
                r = mid - 1;
            else
                l = mid + 1;
        }
        
        return l;
    }
    
    static int time(int[] piles, int k) {
        int totalHours = 0;
        
        for (int i = 0; i < piles.length; i++) {
            totalHours += Math.ceil((double)(piles[i]) / (double)(k));
        }
        return totalHours;
    }
}