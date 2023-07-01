class Solution {
    public int[] shuffle(int[] nums, int n) {
        int j = n;
        int arr[] = new int[2*n];
        int k = 0, i = 0;
        while (k < arr.length){
         arr[k] = nums[i];
         k++; i++;
         arr[k] = nums[j];
         k++; j++;

        }
        return arr;
    }
}