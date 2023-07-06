class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        double arr[] = new double[m + n];
        
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < m && j < n){
            if (nums1[i] < nums2[j])
            {
                arr[k] = nums1[i];
                i++;
            }
        else
        {
            arr[k] = nums2[j];
            j++;
        }
            
            k++;
        }
        while (i < m){
            arr[k] = nums1[i];
            i++;
            k++;
        }
        
        while (j < n){
            arr[k] = nums2[j];
            j++;
            k++;
        }
        
        int x = arr.length;
        
        if (x % 2 == 1){
            int p = (x + 1) / 2 - 1;
            return arr[p];
        }
          
        else{
            double b = arr[x / 2 - 1] ;
            double c = arr[x / 2];
            return 0.5 * (b + c);
        }
        
        
        
    }
}