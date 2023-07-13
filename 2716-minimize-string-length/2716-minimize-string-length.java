class Solution {
    public int minimizedStringLength(String s) {
         
        StringBuilder sb = new StringBuilder();
        Set <Character> as = new HashSet<>();
        
        for (int i = 0; i < s.length(); i++){
            if (as.add(s.charAt(i)))
                   sb.append(s.charAt(i));
        }
        
        return sb.length();
            
    }
}