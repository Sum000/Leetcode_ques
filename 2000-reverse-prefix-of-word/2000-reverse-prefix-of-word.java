class Solution {
    public String reversePrefix(String word, char ch) {
       
        int n = word.length();
        
        if (n==1)
            return word;
        
        for (int i = 0; i < n; i++){
            
            if (word.charAt(i) == ch)
                return reverse(word.substring(0, i + 1)) + word.substring(i + 1, n);
            
        }
        
        return word;
    }
    
    public static String reverse(String str){
        
         String res = "";
        int ind = str.length() - 1;
        for (int i = 0; i < str.length(); i++){
             res += str.charAt(ind);
            ind--;
        }
        return res;
        
    }
    
}