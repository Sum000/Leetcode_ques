class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        
       Set<Integer> n1 = new HashSet<>();
       Set<Integer> n2 = new HashSet<>();
        
        for (int i: nums1)
            n1.add(i);
        
        for (int i:nums2)
            n2.add(i);
        
        List<List<Integer>> ans = new ArrayList<>();
        
        List<Integer> l1 = new ArrayList<>();
        
        for (int i: n1){
            if (!n2.contains(i))
                l1.add(i);
        }
        
        ans.add(l1);
        
        List<Integer> l2 = new ArrayList<>();
        
        for (int i: n2){
            if (!n1.contains(i))
               l2.add(i);
            }
        
        ans.add(l2);
        return ans;
    }
}