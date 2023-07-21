class Solution {
   
    public int strStr(String haystack, String needle) {
        if (haystack.isEmpty())
           return -1;
        
        if (haystack.startsWith(needle)){
           return 0;
        }
        else{

         int index = strStr(haystack.substring(1),needle);
         return (index == -1)? -1: index + 1;
        

        }
          
           
    }
}