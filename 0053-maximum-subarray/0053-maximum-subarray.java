class Solution {
    public int maxSubArray(int[] nums) {
         int n = nums.length;
        int res = nums[0];
        int maxNum = nums[0];
        for(int i=1;i<n;i++){
           maxNum = Math.max(maxNum + nums[i],nums[i]);
           res = Math.max(res,maxNum);
        }
        return res;
    }
}