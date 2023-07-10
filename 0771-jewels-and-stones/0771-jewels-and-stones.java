class Solution {
    public int numJewelsInStones(String jewels, String stones) {
           int m = jewels.length();
        int n = stones.length();
        int count = 0;
        char ch;
        
        for (int i = 0; i < m; i++){
            
            ch = jewels.charAt(i);
            for (int j = 0; j < n; j++){
                
                if (ch == stones.charAt(j))
                    count++;
            }
        }
        
        return count;
    }
}