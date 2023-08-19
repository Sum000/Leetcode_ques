class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res = Integer.MAX_VALUE;
        int left = 0;
        int sum = 0;
        
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            
             while (sum >= target) {
                res = Math.min(res, i - left + 1);
                sum -= nums[left++];
            }
        }
        
        if (res == Integer.MAX_VALUE)
            return 0;
        else
            return res;
         
    }   
     
}