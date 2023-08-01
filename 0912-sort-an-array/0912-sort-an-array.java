class Solution {
    public int[] sortArray(int[] nums) {
         int n = nums.length;
        mergeSort(nums, 0, n - 1);
        return nums;
    }
     public static void merge(int[] nums, int p, int q, int r) {
        int[] res = new int[nums.length];
        int i = p, j = q + 1;
        int k = p; // Start merging from the beginning of the original array.

        while (i <= q && j <= r) {
            if (nums[i] < nums[j]) {
                res[k] = nums[i];
                i++;
            } else {
                res[k] = nums[j];
                j++;
            }
            k++;
        }

        while (i <= q) {
            res[k] = nums[i];
            i++;
            k++;
        }

        while (j <= r) {
            res[k] = nums[j];
            j++;
            k++;
        }

        // Copy the merged array 'res' back to the original 'nums'.
        for (int m = p; m <= r; m++) {
            nums[m] = res[m];
        }
    }

    public static void mergeSort(int[] nums, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;

            mergeSort(nums, p, q);
            mergeSort(nums, q + 1, r);
            merge(nums, p, q, r);
        }
    }
}