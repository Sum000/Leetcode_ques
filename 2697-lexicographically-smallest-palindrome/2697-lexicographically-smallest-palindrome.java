class Solution {
    public String makeSmallestPalindrome(String s) {
        int n = s.length();
        
        StringBuilder sb = new StringBuilder(s);
        
        if (n == 1)
            return s;
        
        int r = n - 1;
        
        for (int i = 0; i < n / 2;i++){
            
            if(sb.charAt(i) != sb.charAt(r)){
                if ((sb.charAt(i) - 'a') < (sb.charAt(r) - 'a'))
                  sb.setCharAt(r, sb.charAt(i));
                else
                    sb.setCharAt(i, sb.charAt(r));
                
                
            }
            
            r--;
                            
            
        }
        
        return sb.toString();
    }
}